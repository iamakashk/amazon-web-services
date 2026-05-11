# How to Push Docker Images to Docker Hub

---

# Step 1: Create a Docker Hub Account

Go to Docker Hub:

https://hub.docker.com

Create an account if you do not already have one.

Example username:

```bash
akashkamble
```

---

# Step 2: Login to Docker Hub from Terminal

Run:

```bash
docker login
```

You will be asked for:

```text
Username:
Password:
```

Successful output:

```text
Login Succeeded
```

---

# Step 3: Build Your Docker Image

Example:

```bash
docker build -t myapp .
```

Check available images:

```bash
docker images
```

Example output:

```text
REPOSITORY   TAG       IMAGE ID
myapp        latest    abc123
```

---

# Step 4: Tag the Image for Docker Hub

Docker Hub image format:

```text
dockerhub-username/image-name:tag
```

Example:

```bash
docker tag myapp akashkamble/myapp:latest
```

Verify:

```bash
docker images
```

Now you should see:

```text
akashkamble/myapp   latest
```

---

# Step 5: Push Image to Docker Hub

Run:

```bash
docker push akashkamble/myapp:latest
```

Docker will upload image layers one by one.

Successful output:

```text
latest: digest: sha256:xxxx
```

---

# Step 6: Verify on Docker Hub

Open:

```text
https://hub.docker.com/r/<username>/<repo>
```

Example:

```text
https://hub.docker.com/r/akashkamble/myapp
```

---

# Complete Example

```bash
# Build image
docker build -t myapp .

# Login
docker login

# Tag image
docker tag myapp akashkamble/myapp:v1

# Push image
docker push akashkamble/myapp:v1
```

---

# Pulling the Same Image Later

Anyone can run:

```bash
docker pull akashkamble/myapp:v1
```

Then:

```bash
docker run akashkamble/myapp:v1
```

---

# Important Docker Concepts

## docker build

Creates an image locally.

```bash
docker build
```

---

## docker tag

Renames image into Docker Hub format.

```bash
docker tag
```

---

## docker push

Uploads image to Docker Hub.

```bash
docker push
```

---

# Common Errors

## denied: requested access to the resource is denied

Possible reasons:

- Wrong Docker Hub username
- Forgot to run `docker login`
- Repository name mismatch

---

## repository does not exist

Your image name format is incorrect.

Correct:

```text
username/repository
```

Wrong:

```text
repository
```

---

# Best Practice for Tags

Instead of always using `latest`:

```text
akashkamble/myapp:v1
akashkamble/myapp:v2
akashkamble/myapp:prod
akashkamble/myapp:dev
```

---

# Real DevOps Workflow

```text
Code → Docker Build → Docker Push → Kubernetes Pull
```

Kubernetes clusters pull images directly from Docker Hub.

---

# Example with Angular Application

```bash
docker build -t angular-app .

docker tag angular-app akashkamble/angular-app:v1

docker push akashkamble/angular-app:v1
```

Example Kubernetes deployment:

```yaml
image: akashkamble/angular-app:v1
```
