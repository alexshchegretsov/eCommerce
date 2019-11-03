<h1 align="center">eCommerce</h1>
<p align="center"><img src="images/Screenshot from 2019-07-11 03-37-58.png" width=650px></p>
<p align="center"><img src="images/Screenshot from 2019-07-11 03-38-18.png" width=650px></p>
<h2>Getting started</h2>
<p>Clone the source locally:</p>
<pre> 
      $ git clone https://github.com/alexshchegretsov/eCommerce.git
      $ cd eCommerce
</pre>

<p>Run containers with "docker-compose" tool:</p>
<pre>
      $ docker-compose up -d
</pre>
<p>Initialize postgres and collect staticfiles:</p>
<pre>
      $ docker-compose run --rm web ./manage.py migrate
      $ docker-compose run --rm web ./manage.py collectstatic    (type "yes")
</pre>

<p>Create site administrator:</p>
<pre>
      $ docker-compose run --rm web ./manage.py createsuperuser
</pre>

<p>Open your browser in a new window, go to admin-panel and log in, for this you need to enter in the input line:</p>
<pre>
      http://127.0.0.1:8000/admin
</pre>
<p><b>Add category and products images from MEDIA directory</b></p>
<h2>Built with</h2>
<ul>
  <li><a href="https://www.djangoproject.com/">Django</a> - The web framework used</li>
  <li><a href="https://mdbootstrap.com/">MDBootstrap</a> - Material Design for Bootstrap</li>
</ul>
<h2>License</h2>
<p>FREE &copy; <a href="https://github.com/alexshchegretsov">Alex Shchegretsov</a></p>
