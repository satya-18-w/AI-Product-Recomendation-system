from langchain_astradb import AstraDBVectorStore
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from src.data.data_creation import DataCreator
from src.config import Config

file_path="./data/main/flipkart_product_review.csv"
class DataIngestion:
    
    def __init__(self):
        self.config=Config()
        self.embedding=HuggingFaceEmbeddings(model_name=self.config.EMBEDDING_MODEL)
        
        self.vectorstore=AstraDBVectorStore(embedding=self.embedding,collection_name="flipkart",api_endpoint=self.config.ASTRA_DB_API_ENDPOINT,
                                            token=self.config.ASTRA_DB_APPLICATION_TOKEN,namespace=self.config.ASTRA_DB_KEYSPACE)
        
        
        
    def ingest(self,load_existing=True):
        if load_existing == True:
            return self.vectorstore
    
    
    
        docs=DataCreator(file_path).convert()
        self.vectorstore.add_documents(docs)
        return self.vectorstore
        
        
        
if __name__ == "__main__":
    ing=DataIngestion()
    ing.ingest(load_existing=False)