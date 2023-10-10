<script>
	/** @type {any} */
	export let trees;
</script>

<svelte:head>
	<title>My planted trees</title>
</svelte:head>

<h2>My trees</h2>

<ul>
	{#each trees.response as { id, tree }}
		<li>
			{tree.name}
		</li>
	{/each}
</ul>
