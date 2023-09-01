<script>
	import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { goto } from '$app/navigation';
	export let data;

		/**
	 * @param {{ detail: { signout: any; }; }} event
	 */
	 async function handleLogout(event) {
		const status = event.detail.signout;
		await goto(`/?signout=${status}`);
	}
</script>

<div class="app">
	<Navbar user={data.user} on:logout{handleLogout} />
	<div class="slot">
		<slot />
	</div>
	<Footer />
</div>

<style>
	.app {
		font-family: 'Lato', 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans',
			Arial, sans-serif;
	}

	.slot {
		min-height: 75vh;
		margin-top: 85px;
	}
</style>
