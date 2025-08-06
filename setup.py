from setuptools import setup, find_packages

setup(
    name='universal-offline-ai-chatbot',
    version='0.1.0',
    author='Aditya Bhatt',
    author_email='info.adityabhatt3010@gmail.com',
    description='Universal Offline AI Chatbot powered by local Mistral + FAISS + LangChain',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AdityaBhatt3010/Universal-Offline-AI-Chatbot',
    license='MIT',
    packages=['src'],  # only `src` as code container
    include_package_data=True,
    install_requires=[
        'streamlit>=1.33.0',
        'langchain>=0.2.0',
        'langchain-community>=0.2.0',
        'langchain-core>=0.2.0',
        'langchainhub>=0.1.15',
        'sentence-transformers>=2.2.2',
        'faiss-cpu>=1.7.4',
        'pypdf>=3.9.1',
        'python-dotenv>=1.0.1',
        'pyfiglet>=1.0.2',
        'termcolor>=2.3.0',
        'rich>=13.7.0'
    ],
    entry_points={
        'console_scripts': [
            'universal-ai-cli=main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
