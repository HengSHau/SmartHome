import asyncio
from tapo import ApiClient
import os
from dotenv import load_dotenv

loaded = load_dotenv()

async def main():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    ip_address = os.getenv("IP_ADDRESS")
    
    # 2. Connect to the Tapo Client
    client = ApiClient(tapo_username, tapo_password)
    
    # Specify that we are connecting to a P110 model
    device = await client.p110(ip_address)
    
    print("\nTurning the plug OFF...")
    await device.off()
    
    
    # 4. Fetch device information and energy usage
    device_info = await device.get_device_info()
    print("\n--- Device Info ---")
    print(device_info.to_dict())
    
    energy_usage = await device.get_energy_usage()
    print("\n--- Energy Usage ---")
    print(energy_usage.to_dict())
    

if __name__ == "__main__":
    asyncio.run(main())