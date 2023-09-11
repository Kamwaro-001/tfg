// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			user: {
				logged_in: boolean;
				token: string;
			}
			profile: {
				username: any;
				email: any;
				first_name: any;
				last_name: any;
				phone_number: any;
				town: any;
				county: any;
			}
		}
		// interface PageData {}
		// interface Platform {}
	}
}

export {};
