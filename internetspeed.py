import speedtest

# Set up a speedtest client
st = speedtest.Speedtest()
st.get_best_server()

# Get server location information
server = st.get_best_server()
server_location = f"{server['name']} ({server['country']})"

# Run the speedtest and get download and upload speeds
download = st.download() / 1000000
upload = st.upload() / 1000000

# Print the results
print(f"Server Location: {server_location}")
print(f"Download Speed: {download:.2f} Mbps")
print(f"Upload Speed: {upload:.2f} Mbps")

