# django-restframework-apis
Implementation of various concepts of django rest framework by creating various restful apis.


<h2>Setting Up Environment</h2>
<ol>
  <li>
     Create a virtual environment using command <pre>python -m virtualenv django-env</pre>
  </li>
  
  
  <li>
      Activate the virtual env and install the dependencies using the requirement.txt file. 
    <ul>
      <li>For activating in macOS or Linux based systems <pre>source django-env/bin/activate</pre></li>        
      <li>For activating the Windows<pre>django-env\Scripts\activate</pre></li>
      <li>Install using requirements.txt<pre>pip install -r requirements.txt</pre></li>
    </ul>    
  </li>
</ol>
 
<h2>Enabling the Admin Account</h2>
<ol>
  <li>
     Enable the admin account 
    <pre>python manage.py migrate</pre>
    <pre>python manage.py createsuperuser</pre>
  </li>
</ol>

<h2>Start the webserver</h2>
<ol>
  <li>Webserver will start at http://127.0.0.1:8000 <pre>python manage.py runserver</pre>
  </li>
</ol>

