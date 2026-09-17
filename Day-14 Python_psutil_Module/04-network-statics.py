
import psutil

# Returns network I/O statistics.
network = psutil.net_io_counters()
print(network)
print(network.bytes_sent)
print(network.bytes_recv)

# Returns network interface addresses.
interfaces = psutil.net_if_addrs()
print(interfaces)


# On your Mac, en0 is commonly a primary network interface, though interface names can vary.
for interface, addresses in psutil.net_if_addrs().items():
    print(interface)

    for address in addresses:
        print(address.address)


# Returns network interface status.
stats = psutil.net_if_stats()
for interface, info in stats.items():
    print(interface, info.isup)
