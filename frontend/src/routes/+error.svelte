<script>
	import { page } from '$app/stores';
</script>

<svelte:head>
  <title>404 - Page not found</title>
</svelte:head>

<div class="error-pg justify-content-center">
	<div class="error">
		<h1>404</h1>
		<p class="fw-bold">We couldn't find this page</p>
		<p>
			The requested URL {$page.url.pathname} was not found. <br /> If you are sure you entered the right
			address then the page no longer exists.
		</p>
	</div>
</div>

<style>
	.error-pg {
		display: flex;
		align-items: center;
		padding: 30px 0;
		height: 400px;
	}

	.error {
		padding: 15px;
	}

	.error h1 {
		font-size: 60px;
		font-weight: 700;
		margin: 0;
		color: #f9786f;
	}
</style>
