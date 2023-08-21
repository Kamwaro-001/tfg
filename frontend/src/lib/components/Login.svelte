<script>
	let message = '';
</script>

<div class="login text-center">
	<main class="form-signin w-100 m-auto">
		<form>
			<img class="mb-4" src="/images/bw_logo.svg" alt="" width="72" height="57" />
			<h1 class="h3 mb-3 fw-normal">Please login</h1>

			<div class="form-floating">
				<input
					name="email"
					type="email"
					class="form-control"
					id="floatingInput"
					placeholder="name@example.com"
					required
				/>
				<label for="floatingInput">Email address</label>
			</div>
			<div class="form-floating">
				<input
					name="password"
					type="password"
					class="form-control"
					id="floatingPassword"
					placeholder="Password"
					required
				/>
				<label for="floatingPassword">Password</label>
			</div>

			<button class="w-100 mt-2 btn btn-lg btn-success" type="submit">Login</button>

			<div class="auth-extras">
				<p class="mt-3 mb-3 text-muted">
					<a href="#">Forgot password?</a><br />
					Don't have an account? <a href="/signup">Create account here</a>
				</p>
			</div>
			{#if message !== ''}
				<div class="form-group">
					<div class="alert alert-danger" role="alert">
						{message}
					</div>
				</div>
			{/if}
		</form>
	</main>
</div>

<style>
	.login {
		display: flex;
		align-items: center;
		padding-top: 40px;
		padding-bottom: 40px;
		/* background-color: #f5f5f5; */
	}

	.form-signin {
		max-width: 370px;
		padding: 15px;
		background-color: #f9f7f7;
		border-radius: 0.5em;
		box-shadow: 0 2px 6px 0 rgb(218 218 253 / 65%), 0 2px 6px 0 rgb(206 206 238 / 54%);
	}

	.form-signin label {
		color: #5d5d5d;
	}

	.form-signin .btn {
		border-radius: 5px;
	}

	.form-signin .form-floating:focus-within {
		z-index: 2;
	}

	.form-signin input[type='email'] {
		margin-bottom: -1px;
		border-bottom-right-radius: 0;
		border-bottom-left-radius: 0;
	}

	.form-signin input[type='password'] {
		margin-bottom: 10px;
		border-top-left-radius: 0;
		border-top-right-radius: 0;
	}

	.form-signin .auth-extras {
		text-align: left;
	}

	.auth-extras a {
		text-decoration: none;
		color: green;
	}
</style>
