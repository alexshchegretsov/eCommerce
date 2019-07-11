<h1 align="center">eCommerce</h1>
<p align="center"><img src="images/Screenshot from 2019-07-11 03-37-58.png" width=650px></p>
<p align="center"><img src="images/Screenshot from 2019-07-11 03-38-18.png" width=650px></p>
<h2>Getting started</h2>
<p>Clone the source locally:</p>
<pre> 
      $ git clone https://github.com/alexshchegretsov/TODO_manager.git
      $ cd TODO_manager
</pre>
<p>Update package list and install pip for Python 3:</p>
<pre>
      $ sudo apt update
      $ sudo apt install python3-pip
</pre>
<p>Once the installation is complete, verify the installation by checking the pip version:</p>
<pre>
      $ pip3 --version
</pre>
<p>You are still at /TODO_manager/ directory, create and run virtual environment:</p>
<pre>
      $ virtualenv -p python3.7 .venv
      $ source .venv/bin/activate
</pre>
<h4>Install all dependencies from requirements.txt:</h4>
<pre>
      $ pip3 install -r requirements.txt
</pre>
<p>Move to /src/ directory, initialize data base and run server:</p>
<pre>
      $ cd src/
      $ ./manage.py migrate
      $ ./manage.py runserver
</pre>
<p>Open your browser in a new window and go to localhost, for this you need to enter in the input line:</p>
<pre>
      http://127.0.0.1:8000/
</pre>
