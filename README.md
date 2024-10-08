# HPA and Ingress with Kubernetes

## Setup de environment
0. First you need a cluster created in some cloud platform

1. Clone the repo
```
git clone git@github.com:AlejandrVilla/k8s-ingress-hpa-.git
```
2.  Install Ingress Nginx Controller in your cluster
[Ingress Nginx Controller](https://kubernetes.github.io/ingress-nginx/deploy/ "Ingress Nginx Controller")
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.2/deploy/static/provider/cloud/deploy.yaml
```

3. Check Ingress Nginx pods
```
kubectl get pods -n ingress-nginx
```

## Run deployments, services and use Ingress Nginx

1.  Run the deployments
```
kubectl apply -f backend-dep.yaml
kubectl apply -f frontend-dep.yaml
```

2. Run the services
```
kubectl apply -f backend-svc.yaml
kubectl apply -f frontend-svc.yaml
```

3. Run ingress-nginx.yaml
	- Ingress Nginx will provide a public IP Adress for the services
```
kubectl apply -f ingress.yaml
```

4. Check the services using Ingress or access from your browser
```
curl -X GET http://[IP-Address]/
curl -X GET http://[IP-Address]/backend
```

## Use HPA (Horizontal Pod Autoscaling)
1. Install the metrics in your cluster [HPA blog](https://medium.com/@yakuphanbilgic3/exploring-horizontal-pod-autoscaling-in-kubernetes-5e84d1b25202)
```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

2. Run the hpa
```
kubectl apply -f hpa.yaml
```

3. Create the stress.sh script and add the following code:
```bash
#! /bin/bash
while true;
do
 wget -q -O- http://[IP address]/backend; 
done
```

4. Alternatively use the frontend UI from your browser

5. Check how the cluster scales the pods and resources used
```
kubectl get all
```
or
```
kubectl get hpa
```