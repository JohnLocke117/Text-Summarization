<h1 align="center">Text Summarization</h1>

<h1>Methodoloy:</h1>
A text summarizer model has been implemented via two Routes, the first one performing Abstract Summarization using the Pegasus Model, while the second one performs Extractive Summarization using the Spacy Library for NLP in Python.

<h3>Method 1: Abstractive Text Summarization via PEGASUS</h3>
Pegasus is a pre-trained Text Summarization model which has been used here for performing the task. The model has been imported from HuggingFace. Pegasus performs abstractive text summarization, which means that it creates a new summary for a given block of text input, which is uniquely created rather than taking excrepts from the input itself. <br />
The implementation is present in the Pegasus Directory.

<h3>Method 2: Extractive Text Summarization via SpaCy</h3>
SpaCy is an open-source advanced natural language processing library. It has been used here to perform extractive summarization, which means this moodel retains only the important parts of a text block and discards the rest. <br />
The implementation is present in the Spacy directory.

<h1>How To Run:</h1>
<h3>Pegasus</h3>
To run the Pegasus model, simply execute the Pegasus.ipynb file inside the Pegasus folder. Make sure to change the location of dataset in the code for it to load into the model.

<h3>Spacy</h3>
To run the Spacy model, you can simply execute the `SpacyMain.ipynb` file. Again, make sure that the datset location is set correctly in the code for it to load into the model.<br/>

Also, a web app also has been created for the Spacy model, where you can Input your text and it will create a summary of the given text. The app has not been deployed as of now, but I plan to do so soon on Vercel, after adding in a feww more features, like directly dragging-and-dropping files from our PC.<br/>

To run the Web App, make sure flask is installed in your System. Then, open a Terminal in the Spacy folder and execute the "app.py" file.
Go-To http://localhost:5000/ on your system to access the application. <br />

![Output2](https://user-images.githubusercontent.com/99555479/235488905-c3ffb438-0ceb-4893-abed-478cff499d40.jpg)
