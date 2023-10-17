# URL Filter Python Script

This Python script is designed to filter and categorize URLs based on user-defined patterns for 
in-scope and not in-scope subdomains. The script takes a list of URLs from a file and categorizes 
them into two groups: URLs matching the in-scope pattern and URLs matching the not in-scope 
pattern.

## Usage

1. Clone this repository to your local machine or download the `filter.py` script.

2. Prepare a text file (`urls.txt`) containing a list of URLs, with one URL per line. For example:

   ```plaintext
   www.domain.com
   net.domain.com
   mail.test.domain.com
   php.test.www.domain.com
   www.domain.org

Run the script by providing the urls.txt file as a command-line argument. Open your terminal and 
execute the following command:
```
python3 filter.py urls.txt
```

Follow the on-screen prompts to input the subdomains for in-scope and not in-scope URLs. For 
example, you can input *,www for in-scope and *.domain.org for not in-scope.

The script will process the URLs and display the results in two categories: "In scope URLs" and 
"Not in scope URLs."

# Customizing Subdomains

The script allows you to customize the subdomains you want to include as in-scope and not in-scope. 
You can use the wildcard * to match any subdomain. For instance, * will match all subdomains, and 
www will match only the www subdomain.

# Example
Here's an example of how the script works:

Suppose you have a urls.txt file containing the following URLs:
```
www.domain.com
net.domain.com
mail.test.domain.com
php.test.www.domain.com
www.domain.org
```

When you run the script and input *,www for in-scope and *.domain.org for not in-scope, the script 
will categorize the URLs as follows:
```
In scope URLs:
www.domain.com
net.domain.com
mail.test.domain.com
php.test.www.domain.com

Not in scope URLs:
www.domain.org
```

This separates URLs that match your criteria into in-scope and not in-scope categories.
