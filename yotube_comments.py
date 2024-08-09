import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
from sqlalchemy import create_engine
import json

# API setup
api_service_name = 'youtube'
api_version = 'v3'
developerkey = '' 

# Load API key from JSON file
with open('key.json', 'r') as file:
    data = json.load(file)
    developerkey = data['api']

yt = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developerkey)

# Function to fetch replies
def get_replies(youtube, parent_id):
    replies = []
    next_page_token = None
    while True:
        reply_request = youtube.comments().list(
            part='snippet',
            parentId=parent_id,
            pageToken=next_page_token,
            textFormat='plainText',
            maxResults=100
        )
        reply_response = reply_request.execute()
        
        for item in reply_response.get('items', []):
            reply = item['snippet']
            replies.append([
                reply['authorChannelId'].get('value', None),
                reply['textDisplay'],
                reply.get('viewerRating', 'none'),
                reply['likeCount'],
                reply['publishedAt'],
                reply.get('updatedAt', reply['publishedAt'])
            ])
        
        next_page_token = reply_response.get('nextPageToken')
        if not next_page_token:
            break
            
    return replies

# Function to fetch comments for a video
def get_comments_for_video(youtube, video_id):
    comments = []
    next_page_token = None
    while True:
        comments_request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            pageToken=next_page_token,
            textFormat='plainText',
            maxResults=100
        )
        comment_response = comments_request.execute()
        
        for item in comment_response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']
            comment_data = [
                comment['authorChannelId'].get('value', None),
                comment['textDisplay'],
                comment.get('viewerRating', 'none'),
                comment['likeCount'],
                comment['publishedAt'],
                comment.get('updatedAt', comment['publishedAt'])
            ]
            
            comments.append(comment_data)
        
        next_page_token = comment_response.get('nextPageToken')
        if not next_page_token:
            break
            
    return comments

# Function to create DataFrame from comments
def create_df(comments):
    if not comments:  # Check if comments list is empty
        print("No data to create DataFrame.")
        return None
    df = pd.DataFrame(comments,
                      columns=["channelId",
                               "textDisplay",
                               "viewerRating",
                               "likeCount",
                               "publishedAt",
                               "updatedAt"]
                      )
    return df

# Function to create database connection
def create_db_connection(database_name):
    try:
        db_connection = create_engine(f"sqlite:///{database_name}.db")
        print("Connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
        db_connection = None
    return db_connection

# Function to insert DataFrame into SQL table
def insert_table(db_connection, df, table_name):
    if df is None or df.empty:  # Check if DataFrame is empty
        print(f"No data available to insert into {table_name}.")
        return
    try:
        df.to_sql(table_name, db_connection, if_exists='replace', index=False)
        print(f"Data entered successfully into {table_name}!")
    except Exception as e:
        print(f"Failed to enter data into {table_name}: {e}")

# Main function to run the data pipeline
def run_data_pipeline():
    video_id = input("Enter Video Id: ")
    
    comments = get_comments_for_video(yt, video_id)
    replies = get_replies(yt, video_id)
    
    df_comments = create_df(comments)
    df_replies = create_df(replies)
    
    db_connect_comments = create_db_connection("comments")
    db_connect_replies = create_db_connection("replies")
    
    if db_connect_comments:
        insert_table(db_connect_comments, df_comments, "Youtube_comments")
    if db_connect_replies:
        insert_table(db_connect_replies, df_replies, "Youtube_replies")

if __name__ == "__main__":
    run_data_pipeline()
