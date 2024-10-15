# Steps: 
# Pre-reliquisite:

   key vault in azure

   cluster enable with service provider and managed identity.

# 0. Create secrets in key vault from azure portal
POSTGRES-USER=cyuser, POSTGRES-PASSWORD=cloudyuga, POSTGRES_DB=cydb

# 1. Build custom postgress image that run with a specified username, pwd and db
   
   Go to folder postgres-image & run the following command,
  
`$docker build -t <acr-name>/custom-postgres-restricted:latest .`

`$docker image push <acr-name>/custom-postgres-restricted:latest  `

# 2. create a client pod with this image to create db table at once.

   Go to folder create-table 
`$kubectl apply -f client-pod.yaml`

`$kubectl exec -it postgres-client -- sh`

`#psql -h postgres -U cyuser -d cydb` , pwd:cloudyuga

`cydb=# CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    rating INTEGER
);
`

`\q`

`exit`

Clean-Up:

`$kubectl delete -f client-pod.yaml`

# 3. Generate rating app image

Go to flask-app folder

`$docker build -t <acr-name>/rating-app:latest .`

`$docker push -t <acr-name>/rating-app:latest`

# 4. Deploy Secret Provider Class to extract Secret from keyvault

Go to rating-app folder

`$kubectl apply -f secret-provider-class.yaml`

# 5. Deploy backend for application

`$kubectl apply -f postgress-deployment.yaml`

# 6. Deploy frontend app 

`$kubectl apply -f rating-app-deployment.yaml`

`$kubectl get svc`

Run your app in the browser with loadbalancer IP.


