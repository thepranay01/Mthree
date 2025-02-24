<hr>
<h1 class="code-line" data-line-start=2 data-line-end=3 ><a id="_Computer_Fundamentals_Notes_2"></a>🎓 <strong>Computer Fundamentals Notes</strong></h1>
<hr>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="_1_What_is_an_Operating_System_OS_6"></a>📌 1. What is an Operating System (OS)?</h2>
<p class="has-line-data" data-line-start="8" data-line-end="9">An <strong>Operating System (OS)</strong> is system software that manages hardware and software resources and provides services for computer programs.</p>
<h3 class="code-line" data-line-start=10 data-line-end=11 ><a id="_Functions_of_an_OS_10"></a>🔹 Functions of an OS:</h3>
<p class="has-line-data" data-line-start="12" data-line-end="13"><img src="https://logicmojo.com/assets/dist/new_pages/images/FOS1.png" alt="OS Functions Diagram"></p>
<p class="has-line-data" data-line-start="15" data-line-end="20">✅ <strong>Process Management</strong> – Handles execution of multiple processes.<br>
✅ <strong>Memory Management</strong> – Allocates and deallocates memory.<br>
✅ <strong>File System Management</strong> – Manages files and directories.<br>
✅ <strong>Device Management</strong> – Controls hardware devices through drivers.<br>
✅ <strong>User Interface</strong> – Provides CLI (Command Line Interface) or GUI (Graphical User Interface).</p>
<hr>
<h2 class="code-line" data-line-start=23 data-line-end=24 ><a id="_2_OS_Installation_23"></a>🛠 2. OS Installation</h2>
<h3 class="code-line" data-line-start=25 data-line-end=26 ><a id="_Steps_to_Install_an_OS_25"></a>📌 Steps to Install an OS:</h3>
<p class="has-line-data" data-line-start="27" data-line-end="33">1️⃣ <strong>Boot from Installation Media</strong> (USB/DVD).<br>
2️⃣ <strong>Choose Language &amp; Preferences</strong>.<br>
3️⃣ <strong>Partition the Hard Drive</strong> (Create new partitions or use existing ones).<br>
4️⃣ <strong>Install System Files</strong>.<br>
5️⃣ <strong>Configure User Accounts &amp; Security Settings</strong>.<br>
6️⃣ <strong>Update Drivers &amp; Install Necessary Software</strong>.</p>
<hr>
<h2 class="code-line" data-line-start=36 data-line-end=37 ><a id="_3_File_Systems_36"></a>📂 3. File Systems</h2>
<p class="has-line-data" data-line-start="38" data-line-end="39">A <strong>File System</strong> organizes and stores data on a storage device.</p>
<h3 class="code-line" data-line-start=40 data-line-end=41 ><a id="_Common_File_Systems_40"></a>📌 Common File Systems:</h3>
<p class="has-line-data" data-line-start="42" data-line-end="46">📌 <strong>FAT32</strong> – Used in USB drives, has a 4GB file size limit.<br>
📌 <strong>NTFS</strong> – Default Windows file system, supports permissions and encryption.<br>
📌 <strong>EXT4</strong> – Default for Linux, supports large files and journaling.<br>
📌 <strong>HFS+ / APFS</strong> – Used in macOS, optimized for SSDs.</p>
<hr>
<h2 class="code-line" data-line-start=49 data-line-end=50 ><a id="_4_Kernel_49"></a>🏗 4. Kernel</h2>
<p class="has-line-data" data-line-start="51" data-line-end="52">The <strong>Kernel</strong> is the core part of the OS that directly interacts with hardware.</p>
<p class="has-line-data" data-line-start="53" data-line-end="54"><img src="https://media.geeksforgeeks.org/wp-content/uploads/20250124124411692602/kernel.webp" alt="Kernel"></p>
<h3 class="code-line" data-line-start=55 data-line-end=56 ><a id="_Types_of_Kernels_55"></a>📌 Types of Kernels:</h3>
<p class="has-line-data" data-line-start="57" data-line-end="60">🔸 <strong>Monolithic Kernel</strong> – All system services run in the same space (e.g., Linux).<br>
🔸 <strong>Microkernel</strong> – Only essential services in kernel mode, others in user space (e.g., Minix).<br>
🔸 <strong>Hybrid Kernel</strong> – Combination of both (e.g., Windows NT, macOS).</p>
<hr>
<h2 class="code-line" data-line-start=62 data-line-end=63 ><a id="_5_Device_Drivers_62"></a>🔧 5. Device Drivers</h2>
<p class="has-line-data" data-line-start="64" data-line-end="65">A <strong>Device Driver</strong> is software that allows the OS to communicate with hardware components.</p>
<h3 class="code-line" data-line-start=66 data-line-end=67 ><a id="_Types_66"></a>📌 Types:</h3>
<p class="has-line-data" data-line-start="68" data-line-end="71">🖥 <strong>Kernel-mode Drivers</strong> – Run at a low level with full system access.<br>
🖱 <strong>User-mode Drivers</strong> – Run in user space, less privileged.<br>
📡 <strong>Virtual Drivers</strong> – Emulate hardware functionality (e.g., virtual network adapters).</p>
<hr>
<h2 class="code-line" data-line-start=74 data-line-end=75 ><a id="_6_System_Services_74"></a>🔄 6. System Services</h2>
<p class="has-line-data" data-line-start="76" data-line-end="77">System services run in the background and perform essential tasks.</p>
<h3 class="code-line" data-line-start=78 data-line-end=79 ><a id="_Examples_78"></a>📌 Examples:</h3>
<p class="has-line-data" data-line-start="80" data-line-end="83">🖨 <strong>Print Spooler</strong> – Manages print jobs.<br>
📅 <strong>Task Scheduler</strong> – Automates scheduled tasks.<br>
🌍 <strong>Web Services</strong> – Handles web-based applications.</p>
<hr>
<h2 class="code-line" data-line-start=86 data-line-end=87 ><a id="_7_Monitoring_Performance_86"></a>📊 7. Monitoring Performance</h2>
<p class="has-line-data" data-line-start="88" data-line-end="89">Performance monitoring helps diagnose system slowdowns and optimize resources.</p>
<h3 class="code-line" data-line-start=90 data-line-end=91 ><a id="_Key_Performance_Metrics_90"></a>📌 Key Performance Metrics:</h3>
<h4 class="code-line" data-line-start=92 data-line-end=93 ><a id="_a_Memory_92"></a>📌 a) Memory:</h4>
<p class="has-line-data" data-line-start="94" data-line-end="96">💾 <strong>RAM Usage</strong> – Amount of used/free memory.<br>
🔄 <strong>Swap Space</strong> – Virtual memory usage.</p>
<h4 class="code-line" data-line-start=97 data-line-end=98 ><a id="_b_CPU_97"></a>📌 b) CPU:</h4>
<p class="has-line-data" data-line-start="99" data-line-end="101">⚙ <strong>CPU Usage</strong> – Percentage of CPU utilization.<br>
📊 <strong>Process Load</strong> – Number of running processes.</p>
<h4 class="code-line" data-line-start=102 data-line-end=103 ><a id="_c_Disk_102"></a>📌 c) Disk:</h4>
<p class="has-line-data" data-line-start="104" data-line-end="106">📀 <strong>Disk Read/Write Speed</strong> – Measures storage performance.<br>
⏳ <strong>I/O Queue Length</strong> – Pending disk operations.</p>
<h4 class="code-line" data-line-start=107 data-line-end=108 ><a id="_d_Network_107"></a>📌 d) Network:</h4>
<p class="has-line-data" data-line-start="109" data-line-end="111">🌐 <strong>Bandwidth Usage</strong> – Data transfer rate.<br>
📉 <strong>Packet Loss</strong> – Percentage of lost data packets.</p>
<h4 class="code-line" data-line-start=112 data-line-end=113 ><a id="_e_General_Counters_112"></a>📌 e) General Counters:</h4>
<p class="has-line-data" data-line-start="114" data-line-end="116">⏳ <strong>Uptime</strong> – System running time since last reboot.<br>
🚨 <strong>System Errors</strong> – Logs of system warnings and failures.</p>
<hr>
<h2 class="code-line" data-line-start=119 data-line-end=120 ><a id="_Summary_Table_119"></a>📜 Summary Table</h2>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Topic</th>
<th>Key Points</th>
</tr>
</thead>
<tbody>
<tr>
<td>OS Functions</td>
<td>Process, Memory, File, Device Management, UI</td>
</tr>
<tr>
<td>OS Installation</td>
<td>Boot, Partition, Install, Configure</td>
</tr>
<tr>
<td>File Systems</td>
<td>FAT32, NTFS, EXT4, HFS+ / APFS</td>
</tr>
<tr>
<td>Kernel Types</td>
<td>Monolithic, Microkernel, Hybrid</td>
</tr>
<tr>
<td>Device Drivers</td>
<td>Kernel-mode, User-mode, Virtual</td>
</tr>
<tr>
<td>System Services</td>
<td>Print Spooler, Task Scheduler, Web Services</td>
</tr>
<tr>
<td>Performance Monitoring</td>
<td>Memory, CPU, Disk, Network, General Counters</td>
</tr>
</tbody>
</table>