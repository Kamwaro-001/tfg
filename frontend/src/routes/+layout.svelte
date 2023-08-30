<script>
	import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<div class="app">
	<Navbar />
	<div class="slot">
		<slot />
	</div>
	<Footer />
</div>

<style>
	.app {
		font-family: 'Lato', 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
	}

	.slot {
		min-height: 75vh;
		margin-top: 85px;
	}
</style>
