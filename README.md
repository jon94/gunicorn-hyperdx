# gunicorn-dd
test gunicorn with local lib injection

- The results show that we can make use of local lib injection to instrument a app that uses gunicorn.

## Simulate Traffic
```
k exec -it hello-world-deployment-75c679dd55-g8wvl -- /bin/bash
```

```
apt-get update && apt-get install -y curl
```

```
curl http://localhost:8000
```
## See in Datadog
<img width="1116" alt="image" src="https://github.com/user-attachments/assets/cc6a7976-d328-4f01-b303-ee7996f9d725">

<img width="1321" alt="image" src="https://github.com/user-attachments/assets/bc1b810f-5beb-4fc4-a325-4d5b9d0539f5">

<img width="1063" alt="image" src="https://github.com/user-attachments/assets/7664940e-447c-4715-910f-b4a4a4320eb5">
