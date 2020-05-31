from .models import graph


def import_database():
    tx = graph.begin()
    tx.run(
        "create (n:PowerSupply {name: 'EVGA SuperNOVA 750 G3', price: '199.99', description: '80 Plus Gold 750W, Fully Modular, Eco Mode with New HDB Fan, 10 Year Warranty, Includes Power ON Self Tester, Compact 150mm Size, Power Supply 220-G3-0750-X1', image:'https://m.media-amazon.com/images/I/51ftf95MTML.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'Seasonic Prime 1000', price: '399.99', description: 'Titanium SSR-1000TR 1000W 80+ Titanium ATX12V, PREMIUM HYBRID FAN CONTROL, MICRO TOLERANCE LOAD REGULATION', image:'https://m.media-amazon.com/images/I/51w25+P4cnL.jpg'})"
    )
    tx.run(
        "create (n:PowerSupply {name: 'Corsair CX Series 550', price: '79.99', description: '550 Watt 80 Plus Bronze Certified Modular Power Supply (CP-9020102-NA), 80 PLUS Bronze certified, Thermally Controlled Fan', image:'https://m.media-amazon.com/images/I/51RxdsALapL.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'CORSAIR RMX Series (2018)', price: '104.19', description: '650 Watt, 80+ Gold Certified, Fully Modular Power Supply, 80 PLUS Gold certified for lower power consumption, Fan Size: 140mm', image:'https://m.media-amazon.com/images/I/51DL07sZNqL.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'EVGA 500 BR', price: '59.94', description: '80+ Bronze 500W, 3 Year Warranty, Power Supply, 80 plus Bronze certified, Heavy-duty protections', image:'https://m.media-amazon.com/images/I/41nsGhBpHYL.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'CORSAIR RMX Series RM750x', price: '117.84', description: '750 Watt, 80+ Gold Certified, Tuned for low noise operation even at full load, 100% industrial-grade', image:'https://m.media-amazon.com/images/I/51Fmty8WPWL.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'Seasonic FOCUS Plus 550', price: '175.99', description: 'Gold SSR-550FX 550W 80+ Gold ATX12V, COMPACT SIZE - 140 MM DEEP, FULL MODULAR, HYBRID SILENT FAN CONTROL', image:'https://m.media-amazon.com/images/I/519H6MYvl4L.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'EVGA 500 W1', price: '55.99', description: '80+ WHITE 500W, Heavy duty protections, including OVP (Over Voltage protection)', image:'https://m.media-amazon.com/images/I/41yjHxdsYQL.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'Thermaltake Smart 500W', price: '44.99', description: '80+ White Certified PSU, Delivers 500 Watt Continuous output @ +40 degree, Supports (2) PCI E 6+2pin Connectors', image:'https://m.media-amazon.com/images/I/51jT3BgFUAL.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'EVGA SuperNOVA 850 G3', price: '244.99', description: '80 Plus Gold 850W, Fan size/ Bearing: 130 millimeters Hydraulic Dynamic Bearing for ultra quiet performance', image:'https://m.media-amazon.com/images/I/51+fhs805bL.jpg'});"
    )
    tx.run(
        "create (n:PowerSupply {name: 'Corsair SF Series SF600', price: '259.99', description: '600 Watt, SFX, 80+ Platinum Certified, Zero RPM fan mode for near-silent operation at low to medium loads', image:'https://m.media-amazon.com/images/I/51u-W1oCMrL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'WD Red 1TB NAS Hard Drive', price: '59.99', description: 'Supports up to 180 TB/yr workload rate, NASware firmware for compatibility', image:'https://m.media-amazon.com/images/I/418Bp7SiimL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'WD Purple 1TB Surveillance Hard Drive', price: '52.88', description: 'RPM:5400 RPM, Cache Memory:64 MB, Interface:SATA 6Gb/s, Type:HDD', image:'https://m.media-amazon.com/images/I/41V8ocBnleL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'Toshiba 1TB Desktop', price: '89.99', description: 'RPM:7200 RPM, Cache Memory:64 MB, Interface:SATA 6Gb/s, Type:HDD', image:'https://images-na.ssl-images-amazon.com/images/I/41JY-wOZglL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'Seagate BarraCuda 1TB Internal Hard Drive HDD', price: '47.99', description: 'RPM:7200 RPM, Cache Memory:64 MB, Interface:SATA 6Gb/s, Type:HDD', image:'https://m.media-amazon.com/images/I/511E7w91IeL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'WD Blue 6TB PC Hard Drive', price: '173.79', description: 'RPM:5400 RPM, Cache Memory:64 MB, Interface:SATA 6Gb/s, Type:HDD', image:'https://images-na.ssl-images-amazon.com/images/I/51gsbTKpaEL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'Seagate Barracuda 4TB Internal Hard Drive HDD', price: '90.73', description: 'RPM:5400 RPM, Cache Memory:256 MB, Interface:SATA 6Gb/s, Type:HDD', image: 'https://m.media-amazon.com/images/I/41+6zb4H2rL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'WD Black 2TB Performance Desktop HDD', price: '118.99', description: 'RPM:7200 RPM, Cache Memory:64 MB, Interface:SATA 6Gb/s, Type:HDD', image:'https://m.media-amazon.com/images/I/51CDaZ7G74L.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'Seagate SkyHawk 1TB Surveillance HDD', price: '39.50', description: 'RPM:5400 RPM, Cache Memory:64 MB, Interface:SATA 6Gb/s, Type:HDD', image: 'https://cdn11.bigcommerce.com/s-zbabt7ht4y/images/stencil/1280x1280/products/40955/62209/seagate-st1000vx005_gmcua__56399.1547990747.jpg?c=2&imbypass=on'});"
    )
    tx.run(
        "create (n:Storage {name: 'CORSAIR FORCE Series MP510 960GB NVMe PCIe Gen3 x4 M.2 SSD', price:'261.39', description: 'RPM:SSD, Cache Memory:N/A, Interface:M.2-2280, Type:SSD', image:'https://m.media-amazon.com/images/I/313Gqmbq5mL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'Samsung 960 EVO 500GB Solid State Drive', price:'177.51', description: 'RPM:SSD, Cache Memory:N/A, Interface:M.2-2280, Type:SSD', image:'https://m.media-amazon.com/images/I/41N9-bYgjsL.jpg'});"
    )
    tx.run(
        "create (n:Storage {name: 'Samsung 970 EVO Plus SSD 250GB - M.2 NVMe Interface Internal Solid State Drive', price: '84.99', description: 'RPM:SSD, Cache Memory:N/A, Interface:M.2-2280, Type:SSD', image:'https://m.media-amazon.com/images/I/41s+xkFOdUL.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'Thermaltake Level 20', price: '999.99', description: 'Cabinet Type:Extended ATX, Alexa - Control fan/LED strip lights or fan speed by talking to Alexa-enabled devices, Razer Chroma - Sync level 20 fan/LED strip RGB lighting with Razer Chroma ecosystem', image:'https://m.media-amazon.com/images/I/51lG15ujD5L.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'CORSAIR Crystal 570X RGB Mid-Tower Case', price: '166.11', description: 'Four tempered glass panels on the front, top, and sides of the case, Room for up to six case fans, and compatible with 360mm, 280mm, 240mm, and 120mm radiators', image: 'https://m.media-amazon.com/images/I/41kJK2zw5rL.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'Thermaltake Tower 900 Black Edition', price: '243.93', description: 'Supports Mini ITX, Micro VAX, ATX, E-ATX Motherboard, 5mm Thick Tempered Glass Window with Stunning Viewing, Eliminates the issue with GPU SAG', image:'https://m.media-amazon.com/images/I/510caltQ-ZL.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'Phanteks Eclipse Steel ATX Mid Tower Tempered Glass Black Case', price: '89.99', description: 'Fully Equipped with Magnetic Dust Filter, Size PSU support, RGB Power Light + Ambient Down Light (10 colors)', image:'https://m.media-amazon.com/images/I/31MpjqkDV9L.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'Phanteks Eclipse P350X (PH-EC350PTG_DBK) Compact EATX Mid-Tower Case', price: '77.15', description: 'Clean interior -PSU Cover & HDDs, Fully Equipped with Magnetic Dust Filter, Size PSU support, Motherboard Support -> ATX, uATX, mITX', image:'https://m.media-amazon.com/images/I/41jlm0Ygc4L.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'CORSAIR Carbide 275R Mid-Tower Gaming Case', price: '68.71', description: 'Full window side panel shows of your system in style, Builder-friendly with simple and intuitive internal layou, Top dust filter not included with standard 275R', image: 'https://m.media-amazon.com/images/I/416itRKTTkL.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'Cooler Master MasterCase H500 ATX Mid-Tower', price: '107.34', description: 'Radiator support: up to 360mm radiator support, Included: light grey tinted temper glass and top magnetic filter on the top panel', image: 'https://m.media-amazon.com/images/I/51F2jz65KtL.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'CORSAIR CARBIDE SPEC-05 Mid-Tower Gaming Case', price: '51.90', description: 'Room for up to five 120mm fans with one 120mm front fan pre-installed, Expansive storage space with mounts for up to three HDDs and two SSDs', image:'https://m.media-amazon.com/images/I/41A2zyKGZiL.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'Thermaltake Versa H15 SPCC Micro ATX Mini Tower Computer Chassis', price: '61.99', description: 'Ideal for home-computer builder Intel & AMD PC systems, Equipped with 1 x 120mm rear turbo fan with optional 2 x 120mm intake fan', image:'https://m.media-amazon.com/images/I/515lScYR8aL.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'Thermaltake View 71 RGB 4-Sided Tempered Glass Vertical GPU Modular E-ATX Gaming Full Tower Computer Case', price: '199.99', description: '4-SIDED GLASS VIEWING PROTECTION, 3-WAY RADIATOR VIEW, VERTICAL GPU, SUPPORT UP TO 10 HDD', image:'https://m.media-amazon.com/images/I/51FntEHQjNL.jpg'});"
    )
    tx.run(
        "create (n:Case {name: 'Fractal Design Meshify C TG Lt', price: '122.12', description: 'A compact yet spacious open ATX layout creates an unrestricted airflow path from front intakes directly through key components to exhaust', image: 'https://m.media-amazon.com/images/I/41HkbdIZKAL.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'Corsair Vengeance LPX 16GB', price: '79.99', description: 'RAM Size:16GB (2 x 8GB), Quantity:2, RAM Type:DDR4-3000', image: 'https://m.media-amazon.com/images/I/41qRQc93t+L.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'CORSAIR VENGEANCE RGB PRO 32GB', price: '189.99', description: 'RAM Size:32GB (4 x 8GB), Quantity:4, RAM Type:DDR4-3200'});"
    )
    tx.run(
        "create (n:RAM {name: 'Corsair LPX 32GB', price: '129.99', description: 'RAM Size:32GB (2 x 16GB), Quantity:2, RAM Type:DDR4-3200', image: 'https://m.media-amazon.com/images/I/31m39tpN7mL.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'CORSAIR VENGEANCE RGB PRO 16GB', price: '92.99', description: 'RAM Size:16GB (2 x 8GB), Quantity:2, RAM Type:DDR4-3200', image: 'https://m.media-amazon.com/images/I/41DvoAGsnrL.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'Corsair Vengeance RGB PRO 32GB', price: '154.99', description: 'RAM Size:32GB (2 x 16GB), Quantity:2, RAM Type:DDR4-3200', image: 'https://m.media-amazon.com/images/I/51dcKTDbLCL.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'CORSAIR Vengeance LPX 8GB', price: '38.99', description: 'RAM Size:8GB (1 x 8GB), Quantity:1, RAM Type:DDR4-2400', image: 'https://images-na.ssl-images-amazon.com/images/I/41Z-epr18JL.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'G.SKILL 32GB (2 x 16GB) Ripjaws V Series', price: '125.99', description: 'RAM Size:32GB (2 x 16GB), Quantity:2, RAM Type:DDR4-3200', image: 'https://images-na.ssl-images-amazon.com/images/I/41WNo3NazQL.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'CORSAIR VENGEANCE RGB PRO 16GB', price: '89.99', description: 'RAM Size:16GB (2 x 8GB), Quantity:2, RAM Type:DDR4-3200', image: 'https://m.media-amazon.com/images/I/51E5dYQRJ2L.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'Team 16GB (2 x 8GB) T-Force Vulcan', price: '99.99', description: 'RAM Size:16GB (2 x 8GB), Quantity:2, RAM Type:DDR4-3000', image: 'https://images-na.ssl-images-amazon.com/images/I/11ADLSBWXLL.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'G.Skill 16GB (2 x 8GB) Ripjaws V Series', price: '72.99', description: 'RAM Size:16GB (2 x 8GB), Quantity:2, RAM Type:DDR4-3200', image: 'https://images-na.ssl-images-amazon.com/images/I/41kjGElfoZL.jpg'});"
    )
    tx.run(
        "create (n:RAM {name: 'Corsair Vengeance LPX 16GB', price: '79.99', description: 'RAM Size:16GB (2 x 8GB), Quantity:2, RAM Type:DDR4-3000', image: 'https://images-na.ssl-images-amazon.com/images/I/31P8eu0IUoL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'EVGA GeForce RTX 2080 Ti Black Edition Gaming', price: '1,499.77', description: 'Memory:11 GB, Clock Speed:1350 MHz, Interface:PCIe x16', image: 'https://m.media-amazon.com/images/I/41g7qQGNckL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'NVIDIA Titan RTX Graphics Card', price: '2,499.99', description: 'Memory:24 GB, Clock Speed:7,000 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/419-U-BzglL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'MSI GAMING GeForce RTX 2080 Ti', price: '1,269.95', description: 'Memory:11 GB, Clock Speed:1350 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/51dfc93wZ%2BL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'EVGA GeForce RTX 2080 Super Black Gaming', price: '815', description: 'Memory:8 GB, Clock Speed:1815 MHz, Interface:PCIe x16', image: 'https://m.media-amazon.com/images/I/41aRAuhk5CL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'MSI VGA Graphic Cards RX 580', price: '189.99', description: 'Memory:8 GB, Clock Speed:1257 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/51jtNWawtYL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'MSI Gaming GeForce GTX 1660 Ti', price: '348.40', description: 'Memory:6 GB, Clock Speed:1500 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/41MvaKfRklL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'ASUS ROG Strix GeForce RTX 2080TI', price: '1,684.38', description: 'Memory:11 GB, Clock Speed:1350 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/516DSMtIqwL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'ASUS GeForce RTX 2080 O8G ROG STRIX OC Edition', price: '1,289.99', description: 'Memory:8 GB, Clock Speed:1,442 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/51D3y0DSXyL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'MSI Gaming Radeon RX 570', price: '169.39', description: 'Memory:8 GB, Clock Speed:1168 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/510bg1-5eJL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'Sapphire Pulse Radeon RX 580', price: '273.20', description: 'Memory:8 GB, Clock Speed:1257 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/51YnzKoOCHL.jpg'});"
    )
    tx.run(
        "create (n:VideoCard {name: 'MSI Computer V809-2277R', price: '158.67', description: 'Chipset:GeForce GTX 1050 Ti, Memory:4 GB, Clock Speed:1341 MHz, Interface:PCIe x16', image: 'https://images-na.ssl-images-amazon.com/images/I/41vnmZp3g7L.jpg'});"
    )
    tx.run(
        "create (n:OperatingSystem {name: 'Microsoft Windows 10 Home OEM 64-bit', price:'108.78', description: 'Type: Windows, Mode: 64-bit, Version: Windows 10 Home, Maximum Supported Memory: 128 GB', image: 'https://cdn.pcpartpicker.com/static/forever/images/product/f5e3c78aadf16d536c31b0fa088c8306.256p.jpg'});"
    )
    tx.run(
        "create (n:OperatingSystem {name: 'Microsoft Windows 10 Pro OEM 64-bit', price: '142.88', description: 'Type: Windows, Mode: 64-bit, Version: Windows 10 Pro, Maximum Supported Memory: 2048 GB', image: 'https://cdn.pcpartpicker.com/static/forever/images/product/e2020af0d40a275d81e0eec3386efa7e.256p.jpg'});"
    )
    tx.run(
        "create (n:OperatingSystem {name: 'Microsoft Windows 10 Pro Full 32/64-bit', price: '189.99', description: 'Type: Windows, Mode: 32/64-bit, Version: Windows 10 Pro, Maximum Supported Memory: 2048 GB', image: 'http://ecx.images-amazon.com/images/I/31y9H18AMUL.jpg'});"
    )
    tx.run(
        "create (n:OperatingSystem {name: 'Microsoft Windows 10 Home Full 32/64-bit', price: '119.04', description: 'Type: Windows, Mode: 32/64-bit, Version: Windows 10 Home, Maximum Supported Memory: 128 GB', image: 'https://onlinemall.rs/wp-content/uploads/2019/07/1436877361_1168590.jpg'});"
    )
    tx.run(
        "create (n:OperatingSystem {name: 'Microsoft Windows 7 Professional Full 32/64-bit', price: '299.00', description: 'Type: Windows, Mode: 32/64-bit, Version: Windows 7 Professional, Maximum Supported Memory: 192 GB', image: 'http://ecx.images-amazon.com/images/I/41UCO5YLmcL.jpg'});"
    )
    tx.run(
        "create (n:OperatingSystem {name: 'Microsoft Windows 7 Home Premium SP1 32-bit', price: '104.99', description: 'Type: Windows, Mode: 32-bit, Version: Windows 7 Home Premium SP1, Maximum Supported Memory: 4 GB', image: 'http://ecx.images-amazon.com/images/I/41EWevTEaqL.jpg'});"
    )
    tx.run(
        "create (n:OperatingSystem {name: 'Microsoft Windows 8.1 OEM 64-bit', price: '129.99', description: 'Type: Windows, Mode: 64-bit, Version: Windows 8.1, Maximum Supported Memory: 128 GB', image: 'http://ecx.images-amazon.com/images/I/31zaL76bdWL.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'Cooler Master Hyper 212 Evo CPU Cooler', price: '34.99', description: 'Fan RPM:600 - 2000 RPM, Noise Level:9 - 36 dB, Color:Black', image: 'https://m.media-amazon.com/images/I/51-VhrzOvwL.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'Cooler Master RR-212S-20PC-R1 Hyper 212 RGB Black Edition CPU Air Cooler', price: '44.99', description: 'Fan RPM:650 - 2000 RPM, Noise Level:8 - 30 dB, Color:Black', image: 'https://m.media-amazon.com/images/I/41d9XZwasVL.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'CORSAIR H100i RGB PLATINUM AIO Liquid CPU Cooler', price: '291.72', description: 'Fan RPM:2400 RPM, Noise Level:37 dB, Color:Black', image: 'https://m.media-amazon.com/images/I/418BKRvC3yL.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'Cooler Master MasterLiquid ML240L RGB AIO CPU Liquid Cooler', price: '61.37', description: 'Fan RPM:650 - 2000 RPM, Noise Level:6 - 30 dB, Color:RGB', image: 'https://m.media-amazon.com/images/I/41CebUQNslL.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'NZXT Kraken X62 280mm - All-In-One RGB CPU Liquid Cooler', price: '126.68', description: 'Fan RPM:500 - 1800 RPM, Noise Level:21 - 38 dB, Color:Black', image: 'https://m.media-amazon.com/images/I/41yU69GPm8L.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'Noctua NH-D15, Premium CPU Cooler', price: '89.95', description: 'Fan RPM:300 - 1500 RPM, Noise Level:19.2 - 24.6 dB, Color:Brown', image: 'https://images-na.ssl-images-amazon.com/images/I/51ls8fys%2BpL.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'be quiet! Dark Rock Pro 4, BK022, 250W TDP, CPU Cooler', price: '89.90', description: 'Fan RPM:1500 RPM, Noise Level:12.8 - 24.3 dB, Color:Black', image: 'https://m.media-amazon.com/images/I/41ALSxzWWZL.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'CORSAIR HYDRO Series H150i PRO RGB AIO Liquid CPU Cooler', price: '262.09', description: 'Fan RPM:1600 RPM, Noise Level:25 dB, Color:RGB', image: 'https://m.media-amazon.com/images/I/51gjr2R138L.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'CORSAIR Hydro Series H60 AIO Liquid CPU Cooler', price: '79.99', description: 'Fan RPM:1700 RPM, Noise Level:28.3 dB, Color:RGB', image: 'https://m.media-amazon.com/images/I/41GBgLCs33L.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'NZXT Kraken X52 240mm - All-In-One RGB CPU Liquid Cooler', price: '149.99', description: 'Fan RPM:500 - 2000 RPM, Noise Level:21 - 36 dB, Color:Black', image: 'https://images-na.ssl-images-amazon.com/images/I/41ogtukvS2L.jpg'});"
    )
    tx.run(
        "create (n:CPUCooler {name: 'ASUS ROG Ryujin 360 RGB AIO Liquid CPU Cooler', price: '379.85', description: 'Fan RPM:450 - 2000 RPM, Noise Level:29.7 dB, Color:Black', image: 'https://images-na.ssl-images-amazon.com/images/I/41pW3WSDbTL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'Intel Core i9-10920X Desktop Processor', price: '1,389.99', description: 'Speed:4.60 GHz, Cores:12, Socket Type:LGA 2066', socket: 'LGA 2066', image: 'https://images-na.ssl-images-amazon.com/images/I/41c09U70gsL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'Intel Core i9-10900X Desktop Processor', price: '659.99', description: 'Speed:4.7 GHz, Cores:10, Socket Type:LGA 2066', socket: 'LGA 2066', image: 'https://images-na.ssl-images-amazon.com/images/I/41W3FebDGuL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'Intel Core i9-10940X Desktop Processor', price: '1,173.89', description: 'Speed:4.8 GHz, Cores:14, Socket Type:LGA 2066', socket: 'LGA 2066', image: 'https://images-na.ssl-images-amazon.com/images/I/41W3FebDGuL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'Intel Core i7-9700K Desktop Processor', price: '374.99', description: 'Speed:3.6 GHz, Cores:8, Socket Type:LGA 1151', socket: 'LGA 1511', image: 'https://images-na.ssl-images-amazon.com/images/I/41i6RHrHrGL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'Intel Core i5-9600K Desktop Processor', price: '169.99', description: 'Speed:3.7 GHz, Cores:6, Socket Type:LGA 1151', socket: 'LGA 1511', image: 'https://images-na.ssl-images-amazon.com/images/I/41ZUZb8cZ5L.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'Intel Core i3-9100F Desktop Processor', price: '59.99', description: 'Speed:3.6 GHz, Cores:4, Socket Type:LGA 1151', socket: 'LGA 1511', image: 'https://images-na.ssl-images-amazon.com/images/I/41XbwAK%2BAyL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'AMD Ryzen Threadripper 3970X', price: '1,899.99', description: 'Speed:4.5GHz, Cores:32, Socket Type:Socket TR4', socket: 'TR4', image: 'https://m.media-amazon.com/images/I/311fbpPo1BL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'AMD Ryzen Threadripper 3960X', price: '1,312.49', description: 'Speed:4.5 GHZ, Cores:24, Socket Type:Socket TR4', socket: 'TR4', image: 'https://m.media-amazon.com/images/I/211M+ujSxDL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'AMD Ryzen 5 3600 6-Core', price: '167.99', description: 'Speed:3.6 GHz, Cores:6, Socket Type:Socket AM4', socket: 'AM4', image: 'https://images-na.ssl-images-amazon.com/images/I/515LB-eoMgL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'AMD Ryzen 7 3800X 8-Core', price: '326.99', description: 'Speed:3.9 GHz, Cores:8, Socket Type:Socket AM4', socket: 'AM4', image: 'https://images-na.ssl-images-amazon.com/images/I/41xUPnTvUSL.jpg'});"
    )
    tx.run(
        "create (n:CPU {name: 'AMD Ryzen 9 3900X 12-core', price: '417.99', description: 'Speed:4.6 GHz, Cores:12, Socket Type:Socket AM4', socket: 'AM4', image: 'https://images-na.ssl-images-amazon.com/images/I/41FswEENgeL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'ASUS ROG X570 Crosshair VIII Formula ATX Motherboard', price: '585.71', description: 'Chipset:AMD X570, Socket Type:Socket AM4, Memory Slot:4', socket: 'AM4', image: 'https://m.media-amazon.com/images/I/51t5mxXQOZL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'ASUS ROG Crosshair VIII Hero X570 ATX Motherboard', price: '351.78', description: 'Chipset:AMD X570, Socket Type:Socket AM4, Memory Slot:4', socket: 'AM4', image: 'https://images-na.ssl-images-amazon.com/images/I/51-bQk%2Bf3HL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'GIGABYTE X399 AORUS Xtreme', price: '955', description: 'Chipset:AMD X399, Socket Type:TR4, Memory Slot:8', socket: 'TR4', image: 'https://m.media-amazon.com/images/I/51XscmKo0jL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'Asus Prime X299 Edition 30 ATX Motherboard (Intel X299) LGA 2066, DDR4 4266 MHz', price: '749.99', description: 'Chipset:Intel X299, Socket Type:LGA 2066, Memory Slot:8', socket: 'LGA 2066', image: 'https://images-na.ssl-images-amazon.com/images/I/418klxJn%2BdL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'ASUS ROG Strix X299-E Gaming II ATX Gaming Motherboard', price: '449.99', description: 'Chipset:Intel X299, Socket Type:LGA 2066, Memory Slot:8', socket: 'LGA 2066', image: 'https://www.asus.com/media/global/products/edqunkuydnrpvmsp/P_setting_000_1_90_end_500.png'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'GIGABYTE X399 AORUS PRO', price: '279.99', description: 'Chipset:AMD X399, Socket Type:TR4, Memory Slot:8', socket: 'TR4', image: 'https://images-na.ssl-images-amazon.com/images/I/51xsbIyIkqL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'Asus ROG Strix Z390-E Gaming Motherboard', price: '239.99', description: 'Chipset:Intel Z390, Socket Type:LGA 1151, Memory Slot:4', socket: 'LGA 1511', image: 'https://images-na.ssl-images-amazon.com/images/I/51PhTUoS9yL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'ASUS ROG Maximus XI Hero (Wi-Fi) Z390 Gaming Motherboard', price: '282.99', description: 'Chipset:Intel Z390, Socket Type:LGA 1151, Memory Slot:4', socket: 'LGA 1511', image: 'https://m.media-amazon.com/images/I/41OHXZOYGNL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'ASUS ROG LGA1151 (300 Series) DDR4 DP HDMI M.2 Mini-ITX Motherboard', price: '249.32', description: 'Chipset:Intel H370, Socket Type:LGA 1151, Memory Slot:4', socket: 'LGA 1511', image: 'https://images-na.ssl-images-amazon.com/images/I/51tn2cTFV8L.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'ASUS Prime X299-Deluxe II X299 Motherboard', price: '479.99', description: 'Chipset:Intel X299, Socket Type:LGA 2066, Memory Slot:8', socket: 'LGA 2066', image: 'https://images-na.ssl-images-amazon.com/images/I/51rcmlgivNL.jpg'});"
    )
    tx.run(
        "create (n:Motherboard {name: 'MSI Arsenal Gaming AMD Ryzen 1st and 2nd Gen AM4 M.2 USB 3 DDR4 DVI HDMI Crossfire ATX Motherboard', price: '109.99', description: 'Chipset:AMD B450, Socket Type:Socket AM4, Memory Slot:4', socket: 'AM4', image: 'https://images-na.ssl-images-amazon.com/images/I/51oIgHDfC0L.jpg'})"
    )
    tx.run(
        "match (cpu:CPU),(motherboard:Motherboard) where cpu.socket=motherboard.socket create (motherboard)-[r:COMPATIBLE]->(cpu)"
    )
    tx.commit()
