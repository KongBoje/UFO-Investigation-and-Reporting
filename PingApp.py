import subprocess

def ping_return(hostname):
    amount = 100
    avg = 0
    result = subprocess.check_output("ping " + hostname, amount).decode("utf-8")
    splitCode = result.split("\n")
    for sc in splitCode:
        if "time=" in sc:
            idx = sc.find('time')
            avg += float(sc[idx+5:-10])
    return round((avg/amount),2)

def the_hosts(list_of_hosts):
    return_sc = dict()
    for hostname in list_of_hosts:
        return_sc[hostname] = ping_return(hostname)

    return return_sc

def main():
    test_hosts = ['128.199.144.199', '167.99.51.33', '46.101.253.149']
    for x in test_hosts:
        ping_return(x)

    print(the_hosts(test_hosts))

if __name__ == '__main__':
    main()