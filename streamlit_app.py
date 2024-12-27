import streamlit as st
from st_files_connection import FilesConnection
from google.oauth2 import service_account
from google.cloud import storage
import pandas as pd

conn = st.connection('gcs', type=FilesConnection)
gcs_file_path = 'mew_test_connection_bucket/file/status.csv'
st.write('connection success', conn)
df = conn.read(gcs_file_path, input_format="csv", ttl=600)
# service_account_info = st.secrets["gcp_service_account"]
# credentials = service_account.Credentials.from_service_account_info(service_account_info)
# client = storage.Client(credentials=credentials)
# buckets = list(client.list_buckets())
# st.write(buckets)

# project_id = 'mew-test-connection-project'
# bucket_name = 'mew_test_connection_bucket'
# file_path = 'file/status.csv'

# bucket = storage.Client(project=project_id).bucket(bucket_name)
# blob = bucket.blob(file_path)
# content = blob.download_as_text()
# df = pd.read_csv(pd.compat.StringIO(content))
st.write(df)