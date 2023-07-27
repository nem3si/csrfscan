<h1>CSRF tester</h1>
<p>The CSRF Vulnerability Scanner is a Python script designed to test web pages for potential Cross-Site Request Forgery (CSRF) vulnerabilities. It performs automated scans on a list of web pages, crafts malicious payloads, and checks for indications of successful unauthorized actions. If a vulnerability is detected, it generates a payload file containing the found payload.</p>


**Note: The script is currently under development, and only a basic logic is provided for demonstration purposes. It may not be suitable for all web applications.**

<h2>Prerequisites</h2>
<p>Before running the script, ensure you have the following installed:</p>
<ul>
  <li>Python 3.x</li>
  <li>Required Python libraries: <code>requests</code>, <code>beautifulsoup4</code></li>
</ul>

<p>You can install the required libraries using <code>pip</code>:</p>

<pre><code>pip install requests beautifulsoup4
</code></pre>

<h2>Usage</h2>
<ol>
  <li>Clone the repository:</li>
</ol>
<pre><code>git clone https://github.com/your-username/csrf-vulnerability-scanner.git
</code></pre>
<ol start="2">
  <li>Navigate to the project directory:</li>
</ol>
<pre><code>cd csrf-vulnerability-scanner
</code></pre>
<ol start="3">
  <li>Prepare a text file (<code>web_pages.txt</code>) containing the list of web pages to scan, with each URL on a separate line.</li>
  <li>Run the script:</li>
</ol>
<pre><code>python scanner.py web_pages.txt
</code></pre>
<ol start="5">
  <li>The scanner will perform the CSRF vulnerability tests for each web page and display the results in the console. If a vulnerability is detected for a specific URL, a payload file (<code>payload_url.txt</code>) will be generated with the malicious payload.</li>
</ol>

<h2>Errors and Troubleshooting</h2>
<p>If you encounter any errors or issues while running the scanner, please ensure that you have the correct prerequisites installed and that the web pages in the input file are accessible. Check the console output for error messages and refer to the <a href="https://github.com/your-username/csrf-vulnerability-scanner/issues">Issues</a> section for known problems and solutions.</p>
