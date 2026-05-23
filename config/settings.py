from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
 api_service_title: str = None
 api_version: str = None
 ollama_base_url: str = None
 vector_db_type: str = None
 chromadb_persist_directory: str = None
 chromadb_collection_name: str = None
 rag_chunk_size: int = None
 rag_chunk_overlap: int = None
 rag_top_k: int = None
 rag_similarity_threshold: float = 0.7
 rag_embedding_model: str = "nomic-embed-text"
 agent_llm_model: str = "llama3"
 agent_temperature: float = 0.0
 agent_max_tokens: int = 4096
 agent_max_iterations: int = 10
 api_host: str = "0.0.0.0"
 api_port: int = 8080
 api_workers: int = 4
 environment: str = "development"
 debug: bool = False
 obs_log_level: str = "INFO"
 obs_log_format: str = "json"
 model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
def get_settings()->Settings:
    return Settings()