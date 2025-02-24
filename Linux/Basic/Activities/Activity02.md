![Linux Logo](https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png)

# Activity: File Systems in Linux

## Creating and Navigating a Directory
```bash
mkdir memory_report
cd memory_report
```

## Listing and Sorting Files by Size in the Home Folder
```bash
du ~ -a | sort -k1,1nr > homefiles_sorted.txt
less homefiles_sorted.txt
```

## Listing and Sorting All Files in the System by Size
```bash
sudo du / -a | sort -k1,1nr > allfiles_sorted.txt
less allfiles_sorted.txt
```

## Checking File Sizes
```bash
du . -ha
ls -la
```

## Checking Available Disk Space
```bash
df -h > filesystems.txt
less filesystems.txt
```

## Creating a Tar Archive of All `.txt` Files
```bash
tar -cvf memory.tar *.txt
```

## Listing the Contents of the Tar Archive
```bash
tar -tvf memory.tar
```

## Compressing the Tar Archive Using Gzip
```bash
gzip memory.tar
```

## Checking the Storage Size After Compression
```bash
du . -ha
```

## Removing Original Files and Checking Disk Usage Again
```bash
rm *.txt
du . -ha
```

## Decompressing and Extracting the Tarball
```bash
gunzip memory.tar.gz
tar -xvf memory.tar
du . -ha
```

## Creating a Compressed Tarball in One Step
```bash
tar -czvf memory.tar.gz *.txt
du . -ha
```

## Extracting the Compressed Tarball
```bash
tar -xzvf memory.tar.gz
du . -ha
```

## Screenshot Section
![Screenshot](https://github.com/thepranay01/Mthree/blob/main/Linux/Basic/Screenshots/Activity_02.png)


