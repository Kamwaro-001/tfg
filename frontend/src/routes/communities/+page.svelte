<script>
	export let data;
</script>

<svelte:head>
	<title>Communities</title>
</svelte:head>

<h2>list of communities</h2>

<ul>
	{#each data.communities as { id, name }}
		<li>
			<a href="/communities/{id}">{name}</a>
		</li>
	{/each}
</ul>
