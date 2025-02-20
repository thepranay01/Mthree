<p class="has-line-data" data-line-start="0" data-line-end="1"><a href="#"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmnqxlkRu175fCZAGTd0O5Wi94y2-sQDRCUg&amp;s" alt="N|Solid"></a></p>
<h1 class="code-line" data-line-start=2 data-line-end=3 ><a id="Git__GitHub_Guide_2"></a>Git &amp; GitHub Guide</h1>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="Introduction_4"></a>Introduction</h2>
<p class="has-line-data" data-line-start="5" data-line-end="6">Git is a distributed version control system that helps track changes in source code during software development. GitHub is a cloud-based platform that provides repositories to host and collaborate on Git projects.</p>
<p class="has-line-data" data-line-start="7" data-line-end="8">This guide covers essential Git commands and their explanations to help you effectively use Git and GitHub.</p>
<hr>
<h2 class="code-line" data-line-start=11 data-line-end=12 ><a id="_Setting_Up_Git_11"></a>🔹 <strong>Setting Up Git</strong></h2>
<p class="has-line-data" data-line-start="12" data-line-end="13">Before using Git, configure your identity:</p>
<pre><code class="has-line-data" data-line-start="15" data-line-end="18" class="language-sh">git config --global user.name <span class="hljs-string">"Your Name"</span>
git config --global user.email <span class="hljs-string">"your.email@example.com"</span>
</code></pre>
<p class="has-line-data" data-line-start="18" data-line-end="19">🔹 <em>Sets your username and email for Git commits.</em></p>
<p class="has-line-data" data-line-start="20" data-line-end="21">Check your Git configuration:</p>
<pre><code class="has-line-data" data-line-start="22" data-line-end="24" class="language-sh">git config --list
</code></pre>
<p class="has-line-data" data-line-start="24" data-line-end="25">🔹 <em>Displays the configured Git settings.</em></p>
<hr>
<h2 class="code-line" data-line-start=28 data-line-end=29 ><a id="_Initializing_a_Git_Repository_28"></a>🔹 <strong>Initializing a Git Repository</strong></h2>
<pre><code class="has-line-data" data-line-start="30" data-line-end="32" class="language-sh">git init
</code></pre>
<p class="has-line-data" data-line-start="32" data-line-end="33">🔹 <em>Creates a new Git repository in the current directory.</em></p>
<hr>
<h2 class="code-line" data-line-start=36 data-line-end=37 ><a id="_Cloning_an_Existing_Repository_36"></a>🔹 <strong>Cloning an Existing Repository</strong></h2>
<pre><code class="has-line-data" data-line-start="38" data-line-end="40" class="language-sh">git <span class="hljs-built_in">clone</span> &lt;repository_url&gt;
</code></pre>
<p class="has-line-data" data-line-start="40" data-line-end="41">🔹 <em>Copies an existing Git repository from GitHub to your local machine.</em></p>
<p class="has-line-data" data-line-start="42" data-line-end="43">Example:</p>
<pre><code class="has-line-data" data-line-start="44" data-line-end="46" class="language-sh">git <span class="hljs-built_in">clone</span> https://github.com/username/repository.git
</code></pre>
<hr>
<h2 class="code-line" data-line-start=49 data-line-end=50 ><a id="_Forking_and_Pull_Requests_49"></a>🔹 <strong>Forking and Pull Requests</strong></h2>
<h3 class="code-line" data-line-start=50 data-line-end=51 ><a id="Forking_a_Repository_50"></a><strong>Forking a Repository</strong></h3>
<pre><code class="has-line-data" data-line-start="52" data-line-end="54" class="language-sh">Go to the repository on GitHub and click <span class="hljs-string">'Fork'</span>
</code></pre>
<p class="has-line-data" data-line-start="54" data-line-end="55">🔹 <em>Creates a copy of a repository in your GitHub account.</em></p>
<h3 class="code-line" data-line-start=56 data-line-end=57 ><a id="Creating_a_Pull_Request_56"></a><strong>Creating a Pull Request</strong></h3>
<ol>
<li class="has-line-data" data-line-start="57" data-line-end="58">Fork the repository.</li>
<li class="has-line-data" data-line-start="58" data-line-end="59">Clone the forked repository.</li>
<li class="has-line-data" data-line-start="59" data-line-end="60">Create a new branch and make changes.</li>
<li class="has-line-data" data-line-start="60" data-line-end="61">Push the branch to your fork.</li>
<li class="has-line-data" data-line-start="61" data-line-end="63">Open a pull request from your branch to the original repository.</li>
</ol>
<hr>
<h2 class="code-line" data-line-start=65 data-line-end=66 ><a id="_Git_Branching_Overview_65"></a>🔹 <strong>Git Branching Overview</strong></h2>
<p class="has-line-data" data-line-start="67" data-line-end="68">Git branching helps in working on multiple features without interfering with the main code. Below is a <strong>Git branching visualization</strong>:</p>
<p class="has-line-data" data-line-start="69" data-line-end="70"><img src="https://i0.wp.com/digitalvarys.com/wp-content/uploads/2019/06/image-7.png?w=1229&amp;ssl=1" alt="Git Branching"></p>
<p class="has-line-data" data-line-start="71" data-line-end="72"><strong>Main Branches in Git:</strong></p>
<ul>
<li class="has-line-data" data-line-start="72" data-line-end="73"><code>main</code> (default branch)</li>
<li class="has-line-data" data-line-start="73" data-line-end="74"><code>feature-branch</code> (new features)</li>
<li class="has-line-data" data-line-start="74" data-line-end="76"><code>hotfix-branch</code> (bug fixes)</li>
</ul>
<p class="has-line-data" data-line-start="76" data-line-end="77">…</p>
<hr>
<h2 class="code-line" data-line-start=80 data-line-end=81 ><a id="_Undoing_Changes__Resetting_Commits_80"></a>🔹 <strong>Undoing Changes &amp; Resetting Commits</strong></h2>
<h3 class="code-line" data-line-start=82 data-line-end=83 ><a id="Undo_Changes_in_a_File_82"></a><strong>Undo Changes in a File</strong></h3>
<pre><code class="has-line-data" data-line-start="84" data-line-end="86" class="language-sh">git checkout -- &lt;file&gt;
</code></pre>
<p class="has-line-data" data-line-start="86" data-line-end="87">🔹 <em>Reverts changes in a file to the last committed version.</em></p>
<h3 class="code-line" data-line-start=88 data-line-end=89 ><a id="Reset_Staged_Files_88"></a><strong>Reset Staged Files</strong></h3>
<pre><code class="has-line-data" data-line-start="90" data-line-end="92" class="language-sh">git reset &lt;file&gt;
</code></pre>
<p class="has-line-data" data-line-start="92" data-line-end="93">🔹 <em>Removes a file from the staging area (but keeps changes).</em></p>
<h3 class="code-line" data-line-start=94 data-line-end=95 ><a id="Reset_to_a_Previous_Commit_94"></a><strong>Reset to a Previous Commit</strong></h3>
<pre><code class="has-line-data" data-line-start="96" data-line-end="98" class="language-sh">git reset --soft &lt;commit_<span class="hljs-built_in">hash</span>&gt;
</code></pre>
<p class="has-line-data" data-line-start="98" data-line-end="99">🔹 <em>Moves HEAD to an older commit but keeps changes staged.</em></p>
<pre><code class="has-line-data" data-line-start="101" data-line-end="103" class="language-sh">git reset --hard &lt;commit_<span class="hljs-built_in">hash</span>&gt;
</code></pre>
<p class="has-line-data" data-line-start="103" data-line-end="104">🔹 <em>Resets to a specific commit and removes all changes.</em></p>
<h3 class="code-line" data-line-start=105 data-line-end=106 ><a id="Revert_a_Commit_105"></a><strong>Revert a Commit</strong></h3>
<pre><code class="has-line-data" data-line-start="107" data-line-end="109" class="language-sh">git revert &lt;commit_<span class="hljs-built_in">hash</span>&gt;
</code></pre>
<p class="has-line-data" data-line-start="109" data-line-end="110">🔹 <em>Creates a new commit that undoes a previous commit without modifying history.</em></p>
<hr>
<h2 class="code-line" data-line-start=113 data-line-end=114 ><a id="_Git_Stash_113"></a>🔹 <strong>Git Stash</strong></h2>
<h3 class="code-line" data-line-start=114 data-line-end=115 ><a id="Stashing_Changes_114"></a><strong>Stashing Changes</strong></h3>
<pre><code class="has-line-data" data-line-start="116" data-line-end="118" class="language-sh">git stash
</code></pre>
<p class="has-line-data" data-line-start="118" data-line-end="119">🔹 <em>Temporarily saves changes without committing.</em></p>
<h3 class="code-line" data-line-start=120 data-line-end=121 ><a id="Viewing_Stashes_120"></a><strong>Viewing Stashes</strong></h3>
<pre><code class="has-line-data" data-line-start="122" data-line-end="124" class="language-sh">git stash list
</code></pre>
<p class="has-line-data" data-line-start="124" data-line-end="125">🔹 <em>Shows a list of stashed changes.</em></p>
<h3 class="code-line" data-line-start=126 data-line-end=127 ><a id="Applying_Stashed_Changes_126"></a><strong>Applying Stashed Changes</strong></h3>
<pre><code class="has-line-data" data-line-start="128" data-line-end="130" class="language-sh">git stash apply
</code></pre>
<p class="has-line-data" data-line-start="130" data-line-end="131">🔹 <em>Restores the most recent stash.</em></p>
<h3 class="code-line" data-line-start=132 data-line-end=133 ><a id="Dropping_a_Stash_132"></a><strong>Dropping a Stash</strong></h3>
<pre><code class="has-line-data" data-line-start="134" data-line-end="136" class="language-sh">git stash drop
</code></pre>
<p class="has-line-data" data-line-start="136" data-line-end="137">🔹 <em>Removes the most recent stash.</em></p>
<hr>
<h2 class="code-line" data-line-start=140 data-line-end=141 ><a id="_Using_gitignore_140"></a>🔹 <strong>Using .gitignore</strong></h2>
<h3 class="code-line" data-line-start=141 data-line-end=142 ><a id="Creating_a_gitignore_File_141"></a><strong>Creating a .gitignore File</strong></h3>
<ol>
<li class="has-line-data" data-line-start="142" data-line-end="143">Create a file named <code>.gitignore</code> in the root directory.</li>
<li class="has-line-data" data-line-start="143" data-line-end="145">Add file patterns to ignore:</li>
</ol>
<p class="has-line-data" data-line-start="145" data-line-end="146">Example:</p>
<pre><code class="has-line-data" data-line-start="147" data-line-end="151" class="language-sh">node_modules/
*.log
.env
</code></pre>
<p class="has-line-data" data-line-start="151" data-line-end="152">🔹 <em>This ignores <code>node_modules</code>, <code>.log</code> files, and <code>.env</code> files.</em></p>
<hr>
<h2 class="code-line" data-line-start=155 data-line-end=156 ><a id="_Solving_Merge_Conflicts_155"></a>🔹 <strong>Solving Merge Conflicts</strong></h2>
<h3 class="code-line" data-line-start=157 data-line-end=158 ><a id="Example_of_a_Merge_Conflict_157"></a><strong>Example of a Merge Conflict</strong></h3>
<pre><code class="has-line-data" data-line-start="159" data-line-end="165" class="language-html">&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD
&lt;h1&gt;Welcome to My Website&lt;/h1&gt;
=======
&lt;h1&gt;Welcome to Our Website&lt;/h1&gt;
&gt;&gt;&gt;&gt;&gt;&gt;&gt; feature-branch
</code></pre>
<h3 class="code-line" data-line-start=166 data-line-end=167 ><a id="Steps_to_Resolve_a_Merge_Conflict_166"></a><strong>Steps to Resolve a Merge Conflict</strong></h3>
<ol>
<li class="has-line-data" data-line-start="167" data-line-end="171">Identify conflicts using:<pre><code class="has-line-data" data-line-start="169" data-line-end="171" class="language-sh">git status
</code></pre>
</li>
<li class="has-line-data" data-line-start="171" data-line-end="172">Open the conflicting file and <strong>edit manually</strong> by keeping the correct version.</li>
<li class="has-line-data" data-line-start="172" data-line-end="176">Mark as resolved:<pre><code class="has-line-data" data-line-start="174" data-line-end="176" class="language-sh">git add &lt;file&gt;
</code></pre>
</li>
<li class="has-line-data" data-line-start="176" data-line-end="181">Complete the merge:<pre><code class="has-line-data" data-line-start="178" data-line-end="180" class="language-sh">git commit -m <span class="hljs-string">"Resolved merge conflict"</span>
</code></pre>
</li>
</ol>
<hr>
<h2 class="code-line" data-line-start=183 data-line-end=184 ><a id="_Best_Practices_for_Using_Git_183"></a>🔹 <strong>Best Practices for Using Git</strong></h2>
<ol>
<li class="has-line-data" data-line-start="184" data-line-end="185"><strong>Commit frequently:</strong> Keep commits small and meaningful.</li>
<li class="has-line-data" data-line-start="185" data-line-end="186"><strong>Use feature branches:</strong> Work in separate branches and merge frequently.</li>
<li class="has-line-data" data-line-start="186" data-line-end="187"><strong>Communicate with teammates:</strong> Avoid working on the same file at the same time.</li>
<li class="has-line-data" data-line-start="187" data-line-end="189"><strong>Resolve conflicts early:</strong> Merge changes <strong>frequently</strong> instead of waiting too long.</li>
</ol>
<hr>
<h2 class="code-line" data-line-start=191 data-line-end=192 ><a id="Summary_191"></a><strong>Summary</strong></h2>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Action</th>
<th>Command</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Check for conflicts</strong></td>
<td><code>git status</code></td>
</tr>
<tr>
<td><strong>Resolve conflict manually</strong></td>
<td>Edit the file</td>
</tr>
<tr>
<td><strong>Mark as resolved</strong></td>
<td><code>git add &lt;file&gt;</code></td>
</tr>
<tr>
<td><strong>Commit resolution</strong></td>
<td><code>git commit -m &quot;Resolved merge conflict&quot;</code></td>
</tr>
<tr>
<td><strong>Abort merge (if needed)</strong></td>
<td><code>git merge --abort</code></td>
</tr>
<tr>
<td><strong>Avoid conflicts (best practice)</strong></td>
<td><code>git pull</code> before coding, use feature branches, commit frequently</td>
</tr>
</tbody>
</table>
<hr>
<h2 class="code-line" data-line-start=204 data-line-end=205 ><a id="_Conclusion_204"></a>🚀 <strong>Conclusion</strong></h2>
<p class="has-line-data" data-line-start="205" data-line-end="206">This guide covers essential Git commands used in day-to-day development. With these commands, you can manage your code efficiently, collaborate with teams, and track project history effectively.</p>