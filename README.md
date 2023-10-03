# INTERNAL_PORTAL_BACKEND

## Docker Installation for Windows

To install Docker on Windows, follow these steps:
```curl -L "https://github.com/docker/hub-tool/releases/latest/download/hub-windows-amd64.tgz" | tar -xz --strip-components 1 -C /usr/local/bin/```

## Running the Docker Container
 
1. Pull the Couchbase image from Docker Hub:
  ```docker pull couchbase:community-7.2.0```

2. Run the Couchbase container:
  ```docker run -d --name cbdb -p 8091-8094:8091-8094 -p 11210:11210 couchbase:community-7.2.0```

## Configuring Couchbase as a Minimal Single Node Cluster

To configure Couchbase as a minimal single node cluster, follow these steps:

1. Open your web browser and navigate to <http://localhost:8091> to access the Couchbase WebUI.

2. Follow the on-screen instructions to set up your Couchbase cluster.

## Bucket, Scope and Collection (As of Now)

1. Create a bucket `internal-portal`. 
2. Create `user` scope, create collections: `portfolio`  
3. Create `organization` scope, create collections: `employee` , `organization` 
4. Create primary index on each of the collections using following syntax:   
      ```CREATE PRIMARY INDEX ON `portfolio`;```         
      ```CREATE PRIMARY INDEX ON `employee`;```        
      ```CREATE PRIMARY INDEX ON `organization`;```    

5. Create secondary index on  (for production environment)   
    - `rollNo` field in `user` collection   
    ```CREATE INDEX rollNo ON `portfolio`(rollNo);```   

6. Do the following for executing transactions without errors.     
    - `internal-portal` bucket &#8594; edit &#8594; advanced bucket settings.
    - Under advanced bucket settings, Replicas: Enabled (disable this option)
    - Under advanced bucket settings, set Minimum Durability Level as `Majority`

7. Copy the couchbase connection string, username and password to `COUCHBASE_CONNECTION_STRING`, `COUCHBASE_USERNAME` and `COUCHBASE_PASSWORD`

## Installing the Dependencies

To install the project dependencies, run the following command:
```go mod download```

## Running the Server

To start the server, execute the following command:
```go run main.go```


## now the server is running on port 8080

## Integrating the LCA

### 1. Setup Environment Variables

Make sure you have the necessary environment variables set up before proceeding with the integration process.

### 2. Generate Protocol Buffer Files

1. Navigate to the `src` directory using the following command:

   ```bash
   cd src
   
   1.Set the Go binary path in your PATH using the following command:
   
   export PATH="$PATH:$(go env GOPATH)/bin"

   2. Generate the Protocol Buffer files using protoc. Run the following command:

   protoc --go_out=. --go-grpc_out=. protos/LCA.protoss

