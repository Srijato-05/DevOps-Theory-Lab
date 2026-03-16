#!/bin/bash
# network_setup.sh

# User must define these variables based on their local home network
PARENT_INTERFACE=${1:-eth0}
SUBNET=${2:-192.168.1.0/24}
GATEWAY=${3:-192.168.1.1}
IP_RANGE=${4:-192.168.1.100/30} # Allocating 192.168.1.100 and .101

echo "Creating macvlan network 'backend_macvlan' attached to $PARENT_INTERFACE..."

docker network create -d macvlan \
  --subnet=$SUBNET \
  --gateway=$GATEWAY \
  --ip-range=$IP_RANGE \
  -o parent=$PARENT_INTERFACE \
  backend_macvlan

echo "Network created."
echo "Note: If you are on the host trying to reach 192.168.1.100, Macvlan blocks host-to-container traffic by default."
echo "To fix host-isolation on Linux natively, you would need to create a secondary macvlan interface on the host:"
echo "  sudo ip link add macvlan-bridge link $PARENT_INTERFACE type macvlan mode bridge"
echo "  sudo ip addr add 192.168.1.99/32 dev macvlan-bridge"
echo "  sudo ip link set macvlan-bridge up"
echo "  sudo ip route add 192.168.1.100/31 dev macvlan-bridge"

echo "If using Docker Desktop (Windows/Mac), Macvlan networks are isolated inside the VM and often cannot bridge back to the hypervisor's physical adapter seamlessly without transparent mode."
