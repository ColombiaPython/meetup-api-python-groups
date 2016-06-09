# meetup-api-python-groups
Get the python meetup groups in LATAM and identify the quantity of group members
The result of the execution is saved in
- ./result/colombia.txt 
- ./result/latam.txt 

There is an example of the file output:

# colombia.txt
 =================== Colombia Python groups =================
 Colombia   Bogotá               1098  Django Bogotá 
 Colombia   Medellín             844   Medellín Python y Django Meetup 
 Colombia   Bogotá               689   Bogotá Python Meetup Group 
 Colombia   Bogotá               314   PyData Bogotá 
 Colombia   Barranquilla         214   Django Barranquilla 
 Colombia   Medellín             141   PyLadies Medellín 
 Colombia   Pasto                94    Pasto Python 
 Colombia   Santa Marta          94    Django Santa Marta 
 Colombia   Bogotá               75    [ SDx | Networking | Security | Cloud | Python ] => Colombia 

# latam.txt
 =================== LATAM Python groups ================= 
 Brazil     São Paulo            1953  Grupy-SP   
 Colombia   Bogotá               1098  Django Bogotá 
 Brazil     São Paulo            1058  PyLadies São Paulo 
 Mexico     México City          999   Chilango Django 
 Colombia   Medellín             844   Medellín Python y Django Meetup 
 Colombia   Bogotá               689   Bogotá Python Meetup Group 
 Mexico     México City          677   Pythonista MX 
 Chile      Santiago             552   Python Chile 
 Argentina  Buenos Aires         508   Buenos Aires Python Meetup 
 Peru       Lima                 465   Python Perú 
 Mexico     Monterrey            388   Python Monterrey 
 Uruguay    Montevideo           370   The Montevideo Python Meetup Group 
 Argentina  Buenos Aires         341   Buenos Aires Django Meetup 
 Colombia   Bogotá               314   PyData Bogotá 
 Mexico     México City          245   DjangoMX   
 Colombia   Barranquilla         214   Django Barranquilla 
 Argentina  Buenos Aires         188   Programming for Everybody (Python) - Study Group 
 Mexico     México City          187   Meetup de Python en Ciudad de México 
 Brazil     São Paulo            170   São Paulo Python Meetup 
 Brazil     São Paulo            168   SPython    
 Argentina  Córdoba              167   Córdoba Python Meetup 
 Colombia   Medellín             141   PyLadies Medellín 
 Mexico     México City          131   México City Python Meetup 
 Argentina  La Plata             130   LaPlata.py - Grupo de desarrolladores Python en La Plata 
 Colombia   Santa Marta          94    Django Santa Marta 
 Colombia   Pasto                94    Pasto Python 
 Mexico     México City          92    México City Pyladies Meetup 
 Paraguay   Asunción             77    Python Paraguay 
 Colombia   Bogotá               75    [ SDx | Networking | Security | Cloud | Python ] => Colombia 
 Mexico     México City          50    Python México 
 Mexico     Puebla               42    Meetup de Python en Puebla 

# Setting up the app
Update the MEETUP_API_KEY with the provided api key from meetup.com for your account. The key is located in the
settings.py file

# Running the app
python run.py

# Testing the app
python -m unittest
