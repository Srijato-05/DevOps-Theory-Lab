# Experiment 12: Container Orchestration using Kubernetes

## 1. Objective
To understand why Kubernetes is used, learn its core concepts, and implement deployment, scaling, and self-healing through a hands-on lab using `kubectl`.

## 2. Theory: Why Kubernetes?
While Docker Swarm is simple, **Kubernetes (K8s)** is the industry standard for production environments due to its advanced feature set.

| Reason | Explanation |
| :--- | :--- |
| **Industry Standard** | Most enterprises and cloud providers use Kubernetes. |
| **Powerful Scheduling**| Automatically determines the best node to run your application. |
| **Large Ecosystem** | Extensive support for monitoring, logging, and networking plugins. |
| **Cloud-Native** | Native integration with AWS (EKS), Google Cloud (GKE), and Azure (AKS). |

### Core Concepts Mapping
| Docker Concept | Kubernetes Equivalent | Description |
| :--- | :--- | :--- |
| **Container** | **Pod** | A group of one or more containers. The smallest unit in K8s. |
| **Compose Service**| **Deployment** | Describes the desired state (image, replicas, labels). |
| **Load Balancing** | **Service** | Exposes your app to the outside world with a fixed IP/DNS. |
| **Scaling** | **ReplicaSet** | Ensures the specified number of pod copies are always running. |

---

## 3. Hands-On Lab (Task 1 - 5)

### Prerequisites
- `kubectl` installed on your machine.
- A local cluster running via **k3d** or **Minikube**.

### Task 1: Create a Deployment
A deployment defines which image to use and how many copies (replicas) should run.

1.  **Create `wordpress-deployment.yaml`**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
spec:
  replicas: 2
  selector:
    matchLabels:
      app: wordpress
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - name: wordpress
        image: wordpress:latest
        ports:
        - containerPort: 80
```
2.  **Apply the deployment**:
```bash
kubectl apply -f wordpress-deployment.yaml
```

### Task 2: Expose the Deployment as a Service
Services provide a stable entry point for your temporary pods.

1.  **Create `wordpress-service.yaml`**:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: wordpress-service
spec:
  type: NodePort
  selector:
    app: wordpress
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007
```
2.  **Apply the service**:
```bash
kubectl apply -f wordpress-service.yaml
```

### Task 3: Verify Everything
```bash
# Check pods
kubectl get pods

# Check service
kubectl get svc
```
*Access WordPress at `http://<node-ip>:30007`. (Use `minikube ip` for Minikube or `localhost` for k3d).*

### Task 4: Scale the Deployment
Scale your application from 2 to 4 replicas:
```bash
kubectl scale deployment wordpress --replicas=4
```
*Verify with `kubectl get pods` to see 4 running instances.*

### Task 5: Self-Healing Demonstration
Kubernetes automatically replaces failed or deleted pods.
1. Delete a pod: `kubectl delete pod <pod-name>`
2. Watch Kubernetes recreate it: `kubectl get pods`
*Observation: The Deployment detects the missing pod and starts a new one to reach the desired state of 4 replicas.*

---

## 4. Advanced Lab: Real Cluster with `kubeadm`
For a production-style setup, we use `kubeadm` to bootstrap a cluster on multiple VMs.

### Step 1: Install Packages (All Nodes)
```bash
sudo apt update && sudo apt install -y apt-transport-https ca-certificates curl
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update && sudo apt install -y kubeadm kubelet kubectl
sudo apt-mark hold kubeadm kubelet kubectl
```

### Step 2: Initialize Master Node (Master Only)
```bash
sudo kubeadm init
```

### Step 3: Configure `kubectl` (Master Only)
```bash
mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### Step 4: Install Network Plugin (Calico)
```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

### Step 5: Join Worker Nodes
Run the `kubeadm join` command provided by Step 2 on each worker node.

### Step 6: Verify the Cluster
```bash
kubectl get nodes
```

---

## 5. Summary of Commands (Cheat Sheet)

| Goal | Command |
| :--- | :--- |
| **Apply configuration** | `kubectl apply -f file.yaml` |
| **List pods** | `kubectl get pods` |
| **List services** | `kubectl get svc` |
| **Scale replicas** | `kubectl scale deployment <name> --replicas=N` |
| **Delete a resource** | `kubectl delete <kind> <name>` |
| **Check node status** | `kubectl get nodes` |

---

## 6. Conclusion
This experiment demonstrated the core functionality of Kubernetes: declarative deployments, stable service exposition, easy scaling, and automatic self-healing. While more complex than Docker Swarm, Kubernetes provides the robustness required for enterprise-scale orchestration.
