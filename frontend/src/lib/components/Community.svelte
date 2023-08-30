<div class="create mb-3">
	<form method="post">
		<div class="mb-3">
			<label for="name" class="form-label mb-0">Community name</label>
			<div id="name-help" class="form-text">What the community will be called.</div>
			<input
				type="text"
				class="form-control"
				id="name"
				name="name"
				aria-describedby="name-help"
				required
			/>
		</div>

		<div class="mb-3">
			<label for="region" class="form-label mb-0">Primary region</label>
			<div id="region-help" class="form-text">Which region the community will be based.</div>
			<input
				type="text"
				class="form-control"
				id="region"
				name="region"
				aria-describedby="region-help"
				required
			/>
		</div>

		<div class="mb-3">
			<label for="description">Community description</label>
			<div id="description-help" class="form-text">
				Describe what the community will be mainly doing.
			</div>
			<textarea class="form-control" name="decription" id="description" cols="30" rows="4" />
		</div>

		<label for="">Community visibility</label>
		<div class="form-check">
			<input class="form-check-input" type="radio" name="visibility" id="private" />
			<label class="form-check-label" for="private">
				Private <span class="form-text"> - only people with invitation code can join </span>
			</label>
		</div>
		<div class="form-check">
			<input class="form-check-input" type="radio" name="visibility" id="public" />
			<label class="form-check-label" for="public"
				>Public <span class="form-text"> - anyone can join </span></label
			>
		</div>
		<div class="mt-2">
			<button type="submit" class="btn btn-success w-25">Create</button>
		</div>
	</form>
</div>

<style>
	.create {
		max-width: 500px;
		margin: auto;
		padding: 15px;
		background-color: #f9f7f7;
		border-radius: 0.5em;
		box-shadow: 0 2px 6px 0 rgb(218 218 253 / 65%), 0 2px 6px 0 rgb(206 206 238 / 54%);
	}
	.form-control:focus {
		border-color: #83d299;
		box-shadow: none;
	}

	.form-check {
		margin-bottom: 0.2rem;
	}

	.form-check-input:focus {
		border-color: #83d299;
		box-shadow: none;
	}

	.btn {
		background-color: #83d299;
		border: none;
		color: #343434;
	}

	.btn:hover {
		background-color: #72c387;
	}
</style>
