import time
import datetime

sites = ["www.facebook.com",
         "facebook.com", "www.google.com", "google.com"]
redirect = "127.0.0.1"
hosts_path = "/private/etc/hosts"


def blockSites():
    while (True):
        current_hour = datetime.datetime.now().hour
        if (8 <= current_hour < 16):
            with open(hosts_path, "r+") as file:
                content = file.read()
                for site in sites:
                    if site in content:
                        pass
                    else:
                        file.write(redirect + "\t" + site + "\n")
        else:
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(site in sites for site in line):
                        file.write(line)
                file.truncate()

        time.sleep(60*5)


blockSites()
