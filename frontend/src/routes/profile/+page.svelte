<script>
    /** @type {any} */
    export let data;

    const profile = data.profile

</script>

<svelte:head>
    <title>Profile</title>
</svelte:head>

<h1>Your account settings</h1>

<div class="container">
    <div class="basic">
        <h2>basic information</h2>
        <form method="post">
            <label for="f_name">First name</label>
            <input type="text" name="first_name" id="f_name" bind:value={profile.first_name}>

            <label for="l_name">Last name</label>
            <input type="text" name="last_name" id="l_name" bind:value={profile.last_name}>

            <label for="username">Username</label>
            <input type="text" name="username" id="username" bind:value={profile.username}>

            <label for="email">E-mail</label>
            <input type="email" name="email" id="email" bind:value={profile.email}>

            <label for="p_number">Phone number</label>
            <input type="number" name="phone_number" id="p_number" bind:value={profile.phone_number}>

            <label for="">Address: </label>

            <label for="county">County</label>
            <input type="text" name="county" id="county" bind:value={profile.county}>

            <label for="town">Town</label>
            <input type="text" name="town" id="town" bind:value={profile.town}>

            <button type="submit">Save changes</button>
        </form>
    </div>
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .basic {
        width: 50%;
    }

    h1 {
        text-align: center;
    }

    form {
        display: flex;
        flex-direction: column;
    }

    label {
        margin-top: 1rem;
    }

    input {
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    button {
        margin-top: 1rem;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #ccc;
        cursor: pointer;
    }
</style>
