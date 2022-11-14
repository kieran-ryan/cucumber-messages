<?php

declare(strict_types=1);

/**
 * This code was auto-generated by {this script}[https://github.com/cucumber/messages/blob/main/jsonschema/scripts/codegen.rb]
 */

namespace Cucumber\Messages;

use JsonSerializable;
use Cucumber\Messages\DecodingException\SchemaViolationException;

/**
 * Represents the TestRunFinished message in Cucumber's message protocol
 * @see https://github.com/cucumber/messages
 *
 */
final class TestRunFinished implements JsonSerializable
{
    use JsonEncodingTrait;

    /**
     * Construct the TestRunFinished with all properties
     *
     */
    public function __construct(

        /**
         * Error message. Can be a stack trace from a failed `BeforeAll` or `AfterAll`.
         * If there are undefined parameter types, the message is simply
         * "The following parameter type(s() are not defined: xxx, yyy".
         * The independent `UndefinedParameterType` messages can be used to generate
         * snippets for those parameter types.
         */
        public readonly ?string $message = null,

        /**
         * success = StrictModeEnabled ? (failed_count == 0 && ambiguous_count == 0 && undefined_count == 0 && pending_count == 0) : (failed_count == 0 && ambiguous_count == 0)
         */
        public readonly bool $success = false,

        /**
         * Timestamp when the TestRun is finished
         */
        public readonly Timestamp $timestamp = new Timestamp(),
    ) {
    }

    /**
     * @throws SchemaViolationException
     *
     * @internal
     */
    public static function fromArray(array $arr): self
    {
        self::ensureMessage($arr);
        self::ensureSuccess($arr);
        self::ensureTimestamp($arr);

        return new self(
            isset($arr['message']) ? (string) $arr['message'] : null,
            (bool) $arr['success'],
            Timestamp::fromArray($arr['timestamp']),
        );
    }

    /**
     * @psalm-assert array{message?: string|int|bool} $arr
     */
    private static function ensureMessage(array $arr): void
    {
        if (array_key_exists('message', $arr) && is_array($arr['message'])) {
            throw new SchemaViolationException('Property \'message\' was array');
        }
    }

    /**
     * @psalm-assert array{success: string|int|bool} $arr
     */
    private static function ensureSuccess(array $arr): void
    {
        if (!array_key_exists('success', $arr)) {
            throw new SchemaViolationException('Property \'success\' is required but was not found');
        }
        if (array_key_exists('success', $arr) && is_array($arr['success'])) {
            throw new SchemaViolationException('Property \'success\' was array');
        }
    }

    /**
     * @psalm-assert array{timestamp: array} $arr
     */
    private static function ensureTimestamp(array $arr): void
    {
        if (!array_key_exists('timestamp', $arr)) {
            throw new SchemaViolationException('Property \'timestamp\' is required but was not found');
        }
        if (array_key_exists('timestamp', $arr) && !is_array($arr['timestamp'])) {
            throw new SchemaViolationException('Property \'timestamp\' was not array');
        }
    }
}
