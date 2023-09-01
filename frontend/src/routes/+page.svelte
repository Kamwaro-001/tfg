<script>
	import { page } from "$app/stores";
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<h1>My homepage</h1>
<p>this is the homepage</p>
<p>{$page.data.user.logged_in}</p>
