<script>
	import { onMount } from 'svelte';

	onMount(() => {
		const dropdownBtn = document.querySelectorAll('.dropdown-btn');
		const dropdown = document.querySelectorAll('.dropdown');
		const hamburgerBtn = document.getElementById('hamburger');
		const navMenu = document.querySelector('.menu');
		const links = document.querySelectorAll('.dropdown a');

		function setAriaExpandedFalse() {
			dropdownBtn.forEach((btn) => btn.setAttribute('aria-expanded', 'false'));
		}

		function closeDropdownMenu() {
			dropdown.forEach((drop) => {
				drop.classList.remove('active');
				drop.addEventListener('click', (e) => e.stopPropagation());
			});
		}

		function toggleHamburger() {
			navMenu.classList.toggle('show');
		}

		dropdownBtn.forEach((btn) => {
			btn.addEventListener('click', function (e) {
				const dropdownIndex = e.currentTarget.dataset.dropdown;
				const dropdownElement = document.getElementById(dropdownIndex);

				dropdownElement.classList.toggle('active');
				dropdown.forEach((drop) => {
					if (drop.id !== btn.dataset['dropdown']) {
						drop.classList.remove('active');
					}
				});
				e.stopPropagation();
				btn.setAttribute(
					'aria-expanded',
					btn.getAttribute('aria-expanded') === 'false' ? 'true' : 'false'
				);
			});
		});

		// close dropdown menu when the dropdown links are clicked
		links.forEach((link) =>
			link.addEventListener('click', () => {
				closeDropdownMenu();
				setAriaExpandedFalse();
				toggleHamburger();
			})
		);

		// close dropdown menu when you click on the document body
		document.documentElement.addEventListener('click', () => {
			closeDropdownMenu();
			setAriaExpandedFalse();
		});

		// close dropdown when the escape key is pressed
		document.addEventListener('keydown', (e) => {
			if (e.key === 'Escape') {
				closeDropdownMenu();
				setAriaExpandedFalse();
			}
		});

		// toggle hamburger menu
		hamburgerBtn.addEventListener('click', toggleHamburger);
	});
</script>

<svelte:document />

<header id="nav-menu" aria-label="navigation bar">
	<div class="container">
		<div class="nav-start">
			<a class="nav-brand" href="/">Trees for Growth</a>
			<nav class="menu">
				<ul class="menu-bar">
					<li><a href="/">Home</a></li>

					<li>
						<button
							class="nav-link dropdown-btn"
							data-dropdown="dropdown1"
							aria-haspopup="true"
							aria-expanded="false"
							aria-label="browse"
						>
							Plant
							<i class="bi bi-chevron-down" aria-hidden="true" />
						</button>
						<div id="dropdown1" class="dropdown">
							<ul role="menu">
								<li role="menuitem">
									<a class="dropdown-link" href="/plant">
										<div>
											<span class="dropdown-link-title">Plant</span>
											<p>Add a tree</p>
										</div>
									</a>
								</li>
								<li role="menuitem">
									<a class="dropdown-link" href="/store">
										<div>
											<span class="dropdown-link-title">Store</span>
											<p>Visit the store</p>
										</div>
									</a>
								</li>
							</ul>
						</div>
					</li>

					<li><a href="/about">about</a></li>
				</ul>
			</nav>
		</div>

		<div class="nav-end">
			<div class="right-container">
				<button class="btn btn-success">Signin</button>
			</div>
			<button id="hamburger" aria-label="hamburger" aria-haspopup="true" aria-expanded="false">
				<i class="bi bi-list" aria-hidden="true" />
			</button>
		</div>
		<!-- <nav class="navbar navbar-expand-lg bg-light fixed-top">
			<div class="container">
				<button
					class="navbar-toggler"
					type="button"
					data-bs-toggle="collapse"
					data-bs-target="#navs"
					aria-controls="navs"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span class="navbar-toggler-icon" />
				</button>

				<div class="collapse navbar-collapse" id="navs">
					<ul class="navs navbar-nav me-auto mb-2 mb-lg-0">
						<li class="nav-item active">
							<a class="nav-link" href="/">Home</a>
						</li>
						<li>
							<button class="nav-link dropdown-btn" data-dropdown="dropdown1" aria-expanded="false">
								planting
								<i class="bi bi-chevron-down" aria-hidden="true" />
							</button>
							<div id="dropdown1" class="dropdown">
								<ul>
									<li>
										<a class="dropdown-link" href="/planting">
											<div>
												<span class="dropdown-link-title">Trees</span>
												<p>Plant a tree</p>
											</div>
										</a>
									</li>
									<li>
										<a class="dropdown-link" href="#featured-streams">
											<div>
												<span class="dropdown-link-title">Store</span>
												<p>Visit the store</p>
											</div>
										</a>
									</li>
								</ul>
							</div>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="/about">About</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="/login">login</a>
						</li>
					</ul>
				</div>
			</div>
		</nav> -->
	</div>
</header>

<style>
	#nav-menu {
		border: 1px solid #eeeeee;
	}

	.menu button {
		border: none;
		background-color: transparent;
		cursor: pointer;
		color: inherit;
	}

	.menu ul {
		list-style: none;
	}

	.menu a {
		text-decoration: none;
		color: inherit;
	}

	.btn {
		display: block;
		/* background-color: #2bfb7b; */
		color: white;
		text-align: center;
		padding: 0.6rem 1.4rem;
		font-size: 1rem;
		font-weight: 500;
		border-radius: 5px;
	}

	#nav-menu .container {
		display: flex;
		align-items: center;
		justify-content: space-between;
		column-gap: 2rem;
		height: 90px;
		padding: 1.2rem 3rem;
	}

	.menu {
		position: relative;
		background: white;
	}

	/* .icon {
    padding: 0.5rem;
    background-color: #eeeeee;
    border-radius: 10px;
  }

  .logo {
    margin-right: 1.5rem;
  } */

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

	.menu-bar .dropdown-link-title {
		font-weight: 600;
	}

	.menu-bar .nav-link {
		font-size: 1rem;
		font-weight: 500;
		letter-spacing: -0.6px;
		padding: 0.3rem;
		min-width: 60px;
		margin: 0 0.6rem;
	}

	.menu-bar .nav-link:hover,
	.dropdown-link:hover {
		text-decoration: underline;
	}

	.nav-start,
	.nav-end,
	.menu-bar,
	.right-container {
		display: flex;
		align-items: center;
	}

	.dropdown {
		display: flex;
		flex-direction: column;
		min-width: 230px;
		background-color: white;
		border-radius: 10px;
		position: absolute;
		top: 36px;
		z-index: 1;
		visibility: hidden;
		opacity: 0;
		transform: scale(0.97) translateX(-5px);
		transition: 0.1s ease-in-out;
		box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
	}

	.dropdown .active {
		visibility: visible;
		opacity: 1;
		transform: scale(1) translateX(5px);
	}

	.dropdown ul {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		padding: 1.2rem;
		font-size: 0.95rem;
	}

	.dropdown-btn {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 0.15rem;
	}

	.dropdown-link {
		display: flex;
		gap: 0.5rem;
		padding: 0.5rem 0;
		border-radius: 7px;
		transition: 0.1s ease-in-out;
	}

	.dropdown-link p {
		font-size: 0.8rem;
		color: #636363;
	}

	.right-container {
		display: flex;
		align-items: center;
		column-gap: 1rem;
	}

	#hamburger {
		display: none;
		padding: 0.1rem;
		margin-left: 1rem;
		font-size: 1.9rem;
	}
</style>
