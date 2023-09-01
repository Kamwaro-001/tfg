<script>
	import { createEventDispatcher } from 'svelte';

	/**
	 * @type {any}
	 */
	export let user;
	$: check = user.logged_in;

	const dispatch = createEventDispatcher();

	const handleLogout = () => {
		user = {
			logged_in: false,
			token: '',
		};
		dispatch('logout', { logout: true });
	};
</script>

<header id="nav-menu" class="fixed-top bg-light bg-opacity-75" aria-label="navigation bar">
	<div class="container">
		<div class="nav-start">
			<a class="logo" href="/">
				<img src="/images/color_logo.svg" class="icon" width="57" height="32" alt="Inc Logo" />
			</a>
		</div>
		<div class="nav-mid m-auto">
			<nav class="menu">
				<ul class="menu-bar">
					<li><a href="/">Home</a></li>

					<li class="dropdown">
						<a
							class="nav-link dropdown-toggle"
							href="/plant"
							role="button"
							id="dropdownMenuLink"
							data-bs-toggle="dropdown"
							aria-expanded="false"
						>
							planting
						</a>

						<ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
							<li><a class="dropdown-item" href="/plant">Plant</a></li>
							<li><a class="dropdown-item" href="/store">Store</a></li>
						</ul>
					</li>

					<li class="dropdown">
						<a
							class="nav-link dropdown-toggle"
							href="/communities"
							role="button"
							id="dropdownMenuLink"
							data-bs-toggle="dropdown"
							aria-expanded="false"
						>
							communities
						</a>

						<ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
							<li><a class="dropdown-item" href="/communities">explore</a></li>
							<li><a class="dropdown-item" href="/communities/create">create</a></li>
						</ul>
					</li>

					<li><a class="nav-link" href="/about">about</a></li>
				</ul>
			</nav>
		</div>

		<div class="nav-end">
			{#if check}
				<div class="right-container">
					<a class="nav-link text-success login-link" href="/profile">Profile</a>
					<button class="btn btn-success" on:click={handleLogout}> Sign out </button>
				</div>
			{:else}
				<div class="right-container">
					<a class="nav-link text-success login-link" href="/login">Login</a>
					<button class="btn btn-success">
						<a class="nav-link" href="/signup">Create an account</a>
					</button>
				</div>
			{/if}

			<button id="hamburger" aria-label="hamburger" aria-haspopup="true" aria-expanded="false">
				<i class="bi bi-list" aria-hidden="true" />
			</button>
		</div>
	</div>
</header>

<style>
	#nav-menu {
		border: 1px solid #eeeeee;
		text-transform: capitalize;
	}

	.menu ul {
		list-style: none;
	}

	.menu a {
		text-decoration: none;
		color: inherit;
	}

	.menu a:hover {
		text-decoration: underline;
		color: #72c387;
	}

	.btn {
		display: block;
		background-color: #83d299;
		color: black;
		text-align: center;
		padding: 0.6rem 0.8rem;
		border-style: none;
		font-weight: 600;
	}

	.btn:hover {
		background-color: rgb(147, 217, 167);
	}

	#nav-menu .container {
		display: flex;
		align-items: center;
		justify-content: space-between;
		column-gap: 2rem;
		height: 80px;
		padding: 1.2rem 3rem;
	}

	.menu {
		position: relative;
		font-size: 1rem;
		font-weight: 500;
	}

	.menu-bar li:first-child .dropdown {
		flex-direction: initial;
		min-width: 480px;
	}

	.menu-bar li:first-child ul:nth-child(1) {
		border-right: 1px solid #eeeeee;
	}

	.menu-bar li:nth-child(n + 2) ul:nth-child(1) {
		border-bottom: 1px solid #eeeeee;
	}

	.menu-bar .nav-link {
		font-size: 1rem;
		font-weight: 500;
		letter-spacing: -0.6px;
		padding: 0.3rem;
		min-width: 60px;
		margin: 0 0.6rem;
	}

	.menu-bar .dropdown-item {
		background-color: white;
		font-size: 1rem;
		font-weight: 500;
		letter-spacing: -0.6px;
	}

	.menu-bar .dropdown-menu {
		border: none;
	}

	.nav-start,
	.nav-end,
	.menu-bar,
	.right-container {
		display: flex;
		align-items: center;
	}

	.right-container {
		display: flex;
		align-items: center;
		column-gap: 1rem;
	}

	.right-container .login-link {
		font-weight: bold;
	}

	#hamburger {
		display: none;
		padding: 0.1rem;
		margin-left: 1rem;
		font-size: 1.9rem;
	}
</style>
