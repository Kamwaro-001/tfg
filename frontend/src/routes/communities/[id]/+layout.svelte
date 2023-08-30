<script>
	/** @type {import('./$types').LayoutData} */
	// export let data;
</script>

<div class="layout">
	<slot />
</div>

<style>
    .layout {
        max-width: 80%;
        margin: 0 auto;
        padding: 1rem;
        border: solid 1px #ccc;
        border-radius: 5px;
    }
</style>