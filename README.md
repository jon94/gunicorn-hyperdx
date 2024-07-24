# gunicorn-dd
test gunicorn with local lib injection

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

