# Procedimiento para ejecutar el script

* Clonar el repositorio utilizando visual studio
  - git clone https://github.com/cristianl70/trabajo_backend.git
   
* Cuando se realice eso se debe de ejecutar la maquina virtual, para esto se hará uso del archivo llamado Vagrantfile utilizando los siguientes comandos.
  - vagrant up
  - vagrant ssh

* Finalizada la ejecución del entorno virtual se creará una carpeta llamada mongo que es necesaria para que la base de datos funcione correctamente
  - mkdir mongo

* Luego se accede a la carpeta de vagrant para posteriormente crear una carpeta llamada data.
  - cd vagrant
  - mkdir data
  - cd /vagrant/data/
  - ln -s /home/vagrant/mongo/ .
  - cd ..

* Cuando se haya finalizado los pasos anteriores se debe correr el archivo de docker-compose.yml usando lo siguiente
  - docker-compose up

* Por ultimo, cuando se haya realizado todo satisfactoriamente, por medio de postman se realizan los diferentes ensayos del backend para corroborar la carga de información en la base de datos.
  - Crear paciente: se utiliza el método POST se debe ingresar en formato JSON el backend recibirá cualquier tipo de dato, pero cuando se acople al front-end se va a restringir a los ya establecidos. La URL a utilizar es la siguiente: http://localhost:5000/ingreso-paciente 
  - Editar paciente: se utiliza el método PUT se debe ingresar en formato JSON. La URL a utilizar es la siguiente: http://localhost:5000/ingreso-paciente/{id unico del paciente}
  - Ver paciente: se utiliza el método GET su salida será en formato JSON. La URL a utilizar es la siguiente: http://localhost:5000/ingreso-paciente/{id unico del paciente} o si se requiere ver a todos los pacientes se ingresa la misma URL pero sin el /{id unico del paciente}
  - Eliminar paciente: Se utiliza el metodo DELETE, se debe ingresar la URL con el id del paciente de la siguiente manera. http://localhost:5000/ingreso-paciente/{id unico del paciente}
