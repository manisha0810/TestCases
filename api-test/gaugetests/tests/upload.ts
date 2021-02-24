import { Step } from "gauge-ts";
import { deepStrictEqual, equal } from "assert";
import { Response } from "node-fetch";
import fetch from "node-fetch";

/**
 * All following constants should be read from corresponding environment variables.
 */
export const API_ROUTER_URL = "";
export const API_TOKEN =
  "";

export default class UploadImage {
  private apiVersion: string;
  private path: string;
  private response: Response;



  @Step("Create request to <path>")
  public async setPath(path: string) {
    this.path = path;
  }

  @Step("Send <method> request")
  public async sendRequest(method: string) {
    const requestEndpoint = API_ROUTER_URL + "/" + this.path;
    this.response = await fetch(requestEndpoint, {
      headers: { Authorization: API_TOKEN },
      method
    });
  }

  @Step("Assert that response status code is <code>")
  public async assertStatusCode(code: number) {
    equal(this.response.status, code);
  }

  @Step("Assert that response body is error message with code <code> and message <message>")
  public async assertResponseBodyError(code: string, message: string) {
    const responseBody: ErrorResponse = await this.response.json();
    equal(responseBody.error.code, code);
    equal(responseBody.error.message, message);
  }

  @Step("Assert that response body is not empty")
  public async assertResponseBodyNotEmpty() {
    const responseBody: string = await this.response.text();
    equal(responseBody.length > 0, true);
  }

}

interface ErrorResponse {
  error: {
    code: string;
    message: string;
    target?: string;
  };
}