from langchain_community.document_loaders import DirectoryLoader, UnstructuredExcelLoader, PyPDFLoader, TextLoader

# ドキュメントが保存されているフォルダのパスを指定
documents_folder = "C:\\project\\AI\\RAG"  # 実際のフォルダパスに置き換えてください

# DirectoryLoaderを使ってフォルダ内のドキュメントをロード
loader = DirectoryLoader(
    documents_folder,
    glob="**/*",  # すべてのファイルを対象とする
    loader_cls={
        ".txt": TextLoader,
        ".md": TextLoader,
        ".xlsx": UnstructuredExcelLoader,
        ".pdf": PyPDFLoader,
        ".java": TextLoader, # Javaコードはテキストファイルとして読み込む
    }
)
documents = loader.load()

# テキストを適切なサイズに分割（以前のコードと同じ）
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

print(f"ロードされたドキュメント数: {len(documents)}")
print(f"分割されたチャンク数: {len(chunks)}")