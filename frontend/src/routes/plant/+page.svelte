<script>
	import Plant from '$lib/components/Plant.svelte';
	/** @type {any} */
	export let data;

</script>

<svelte:head>
	<title>My planted trees</title>
</svelte:head>

<h2>My trees</h2>

<ul>
	{#each data.trees as tree}
		<li>
			{tree.more_info}
		</li>
	{/each}
</ul>

<h2>Add a tree</h2>
<Plant />
