#step 1: Load raw pdf
#step 2: divide into chunks
#step 3: embed those chunks
#step 4: store in faiss

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader #to load the pdf and process it 
from lanchain.text_splitter import 