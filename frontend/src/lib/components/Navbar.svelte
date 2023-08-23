<script>
</script>

<header id="nav-menu" class="fixed-top bg-light" aria-label="navigation bar">
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

					<li><a class="nav-link" href="/communities">communities</a></li>
					<li><a class="nav-link" href="/about">about</a></li>
				</ul>
			</nav>
		</div>

		<div class="nav-end">
			<div class="right-container">
				<a class="nav-link text-success login-link" href="/login">Login</a>
				<button class="btn btn-success"
					><a class="nav-link" href="/signup">Create an account</a></button
				>
			</div>
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
	}

	.btn {
		display: block;
		background-color: #308148;
		color: white;
		text-align: center;
		padding: 0.6rem 0.8rem;
		border-style: none;
	}

	.btn:hover {
		background-color: #389a56;
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
