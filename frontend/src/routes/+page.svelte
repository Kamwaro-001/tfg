<script>
	import { page } from "$app/stores";
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<div class="container bg-info">
	<h1>My homepage</h1>
	<p>this is the homepage</p>
	<p>{$page.data.user.logged_in}</p>
	<p class="bg-danger">{$page.data.user.token}</p>
</div>

<style>
	.container {
		padding: 20px;
		max-width: 80%;
	}
</style>