import yaml

with open("deployment.yaml", "r") as file:
    data = yaml.safe_load(file)

print(data)     # it will print whole Deployment file

print(data["apiVersion"]) # apps/v1
print(data["kind"])   # Deployment
print(data["metadata"]["name"])   # axion-deployment
print(data["spec"]["selector"]["matchLabels"]["app"])   # axion-app
print(data["spec"]["template"]["metadata"]["labels"]["app"])    # axion-app
print(data["spec"]["template"]["spec"]["containers"][0]["name"])    # axion-app
print(data["spec"]["template"]["spec"]["containers"][0]["image"])   # nginx:latest
print(data["spec"]["template"]["spec"]["containers"][0]["resources"]["limits"]["memory"])   # 128Mi
print(data["spec"]["template"]["spec"]["containers"][0]["ports"][0]["containerPort"])   # 80



print("--------------------------------------------------------------------------")
with open("svc.yaml", "r") as svcfile:
    svcdata = yaml.safe_load_all(svcfile)   # safe_load_all used to load multiple YAML documents

    for data in svcdata:
        print(data)


print("--------------------------------------------------------------------------")

with open("configmap.yaml", "r") as file:
    data = yaml.full_load(file)
# yaml.full_load(file) works similarly to yaml.safe_load(file), but it uses PyYAML's FullLoader, which supports a broader set of YAML tags/types.

print(data)
print(type(data))