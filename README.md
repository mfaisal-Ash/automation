# automation
Template automation docker, airflow and mongodb
# airflow
template docker-airflow

## Persiapan
--------INDONESIA-----
untuk menjalankan project ini perlu melakukan running dengan perintah di bawah:
`docker-compose -f . \docker-compose-CeleryExecutor.yml up -d `
Perintah tersebut untuk melakukan Installing data kemudian di compare ke dalam docker desktop.
ada perintah untuk uninstall atau remove data pada app docker menggunakan perintah berikut:
`docker-compose -f .\docker-compose-CeleryExecutor.yml down`

Setelah melakukan perintah pertama selanjutnya silakan buat source code atau logic secara mandiri dengan membuat file di folder dags untuk membuat list dags pada dashboard airflow. 

--------ENGLISH-----
SETUP
To run this project, use the following command:

bash
``docker-compose -f ./docker-compose-CeleryExecutor.yml up -d``
This command installs data and syncs it into Docker Desktop. If you need to uninstall or remove data from the Docker app, use this command:

bash

``docker-compose -f ./docker-compose-CeleryExecutor.yml down``
After running the first command, you can proceed to create your custom logic or source code by adding files in the dags folder. This will create a list of DAGs on the Airflow dashboard.




## CONTOH LIST DASHBOARD (EXAMPLE) 
![image](https://github.com/user-attachments/assets/1af97ee6-6a6c-4d14-8ae0-19cbf7cec21f)



selanjutnya silakan buat project sesuai yang ingin di capai, selamat mengerjakan :)

Next Steps: Let's Build the Project You Have in Mind! 🚀

Define the Goal 🎯: Start by clearly outlining what you aim to achieve with this project. Whether it’s data automation, ETL pipelines, or analytics workflows, having a clear objective will keep us focused.

Setup the Project Environment 🛠️:

Make sure Docker is running.
Use docker-compose -f ./docker-compose-CeleryExecutor.yml up -d to launch the Airflow environment.
Verify that all services are running correctly in Docker Desktop.
Create Custom DAGs 📄:

In the dags folder, create Python scripts to define Directed Acyclic Graphs (DAGs) for your workflows.
Each DAG will represent a set of tasks or pipelines within Airflow. Think of tasks such as data extraction, transformation, and loading (ETL).
Test DAGs in Airflow 🧪:

Once your DAGs are defined, go to the Airflow dashboard.
Check that your DAGs appear, then start them and monitor their status and performance.
Continuous Improvement 🔄:

Adjust and iterate on your DAGs as needed to optimize performance and accuracy.
Consider adding additional features or tasks as you go along.
Good luck with your project, and have fun coding! 🎉
