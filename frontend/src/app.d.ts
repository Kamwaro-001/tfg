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
				id: number;
				username: string;
				email: string;
				first_name: string;
				last_name: string;
				phone_number: any;
				town: string;
				county: string;
			}
		}
		// interface PageData {}
		// interface Platform {}
	}
}

export {};
